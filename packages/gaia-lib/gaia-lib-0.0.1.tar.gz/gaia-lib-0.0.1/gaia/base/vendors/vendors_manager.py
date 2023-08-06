import os
import asyncio
import concurrent.futures
import time
import dotenv
from .co_here import CoHereService
from .chat_gpt import ChatGptService

class VendorsManager:
    debug = False
    timer_start = 0
    timer_end = 0
    total_took = 0
    available_vendors = [ChatGptService.name, CoHereService.name]
    compared_vendors = []
    vendors_results = []
    chatGptService=None
    coHereService=None
    def __init__(self, vendors=None, env_file_path=None, api_keys: dict={}, debug=False):
        self.debug = debug
        self.load_env_file(env_file_path=env_file_path)
        chatgpt_key = (os.environ['OPEN_AI_KEY'] if 'OPEN_AI_KEY' in os.environ else (
            api_keys['OPEN_AI_KEY'] if 'OPEN_AI_KEY' in api_keys else ''))
        cohere_key = (os.environ['COHERE_AI_KEY'] if 'COHERE_AI_KEY' in os.environ else (
            api_keys['COHERE_AI_KEY'] if 'COHERE_AI_KEY' in api_keys else ''))
        self.chatGptService = ChatGptService(api_key=chatgpt_key)
        self.coHereService = CoHereService(api_key=cohere_key)
        if vendors is None:
            vendors = self.available_vendors
        self.compared_vendors = vendors

    def load_env_file(self, env_file_path):
        path = '.vendors_keys'
        if env_file_path:
            path = env_file_path
        dotenv_file = os.path.join(path)
        if os.path.isfile(dotenv_file):
            dotenv.load_dotenv(dotenv_file)
    def reset(self):
        self.vendors_results = []
        self.timer_start = 0
        self.timer_end = 0
        self.total_took = 0

    def run_cohere(self, prompt) -> dict:
        prompt_length = len(prompt)
        words_length = len(prompt.split(' '))
        max_tokens = 300 + (words_length * 2) * 3
        text = ''
        total_tokens = 0
        cost = 0
        try:
            prediction = self.coHereService.run_completion(prompt, max_tokens, False)
            text = prediction[0].text
            prompt_tokens = self.coHereService.get_tokens(prompt)
            prediction_tokens = self.coHereService.get_tokens(text)
            total_tokens = prompt_tokens + prediction_tokens
            cost = self.coHereService.get_price(total_tokens)
        except Exception as e:
            text = str(e)
        return {'text': text, 'total_tokens': total_tokens, 'cost': cost}

    def run_chat_gpt(self, prompt) -> dict:
        prompt_length = len(prompt)
        words_length = len(prompt.split(' '))
        max_tokens = 300 + (words_length * 2) * 3
        # prediction = chatGptService.run_completion(prompt, max_tokens, False)
        text = ''
        total_tokens = 0
        cost = 0
        try:
            # text = prediction.choices[0].text
            prediction = self.chatGptService.run_chat(prompt, [], False)
            text = prediction.choices[0].message.content
            prompt_tokens = total_tokens = self.chatGptService.get_tokens(prompt)
            prediction_tokens = total_tokens = self.chatGptService.get_tokens(text)
            total_tokens = prompt_tokens + prediction_tokens
            total_tokens = prediction.usage.total_tokens
            cost = self.chatGptService.get_price(total_tokens)
        except Exception as e:
            text = str(e)
        return {'text': text, 'total_tokens': total_tokens, 'cost': cost}

    async def upper_cased_task(self, vendor: str, prompt: str) -> dict:
        if vendor == ChatGptService.name:
            result = self.run_chat_gpt(prompt)
        if vendor == CoHereService.name:
            result = self.run_cohere(prompt)
        await asyncio.sleep(1)
        return result

    async def chat_gpt_task(self, prompt: str):
        if self.debug:
            print(f"Starting task1 for {prompt}")
        await asyncio.sleep(1)
        result = self.run_chat_gpt(prompt)
        if self.debug:
            print(f"Ending task1 for {prompt}")
        return result

    async def co_here_task(self,prompt: str):
        if self.debug:
            print(f"Starting task2 for {prompt}")
        await asyncio.sleep(1)
        result = self.run_cohere(prompt)
        if self.debug:
            print(f"Ending task2 for {prompt}")
        return result

    async def generic_task(self, vendor: str, prompt: str, index: int) -> dict:
        if self.debug:
            print(f"Starting generic_task in {vendor} for {prompt}")
        result = 'no vendor'
        with concurrent.futures.ThreadPoolExecutor() as executor:
            timer_start = time.perf_counter()
            if vendor == ChatGptService.name:
                result = await asyncio.get_running_loop().run_in_executor(executor, self.run_chat_gpt, prompt)
            if vendor == CoHereService.name:
                result = await asyncio.get_running_loop().run_in_executor(executor, self.run_cohere, prompt)
            timer_stop = time.perf_counter()
            # print('self.vendors_results', self.vendors_results)
            if len(self.vendors_results) and self.vendors_results[index]:
                self.vendors_results[index][f'{vendor}_took'] = f'{timer_stop - timer_start:0.4f}'
        if self.debug:
            print(f"Ending generic_task in {vendor} for {prompt}")
        return result

    async def process_item(self, item: str):
        tasks = []
        obj = {'input': item, 'took': ''}
        for vendor in self.compared_vendors:
            obj[vendor] = ''
            tasks.append(self.generic_task(vendor, item, -1))
        # tasks.append(self.chat_gpt_task(prompt))
        # tasks.append(self.co_here_task(prompt))
        timer_start = time.perf_counter()

        self.vendors_results.append(
            obj
        )
        results = await asyncio.gather(*tasks)
        timer_stop = time.perf_counter()
        if self.debug:
            print(f"Performed {item} on {self.compared_vendors}... {timer_stop - timer_start:0.4f} seconds")
        if self.vendors_results[-1]:
            for idx, vendor in enumerate(self.compared_vendors):
                self.vendors_results[-1][vendor] = results[idx]
            self.vendors_results[-1]['took'] = f'{timer_stop - timer_start:0.4f}'
        # print(f"Results for {item}: {result1}, {result2}")

    async def run_all_parallel(self, prompts: list):
        self.reset()
        self.timer_start = time.perf_counter()
        await self.process_items(prompts)
        self.timer_end = time.perf_counter()
        self.total_took = self.timer_end - self.timer_start

    async def process_items(self, prompts: list):
        tasks = []
        count = 0
        for prompt in prompts:
            obj = {'input': prompt}
            for vendor in self.compared_vendors:
                obj[vendor] = ''
                tasks.append(self.generic_task(vendor, prompt, count))
            self.vendors_results.append(obj)
            count += 1
        # tasks.append(self.chat_gpt_task(prompt))
        # tasks.append(self.co_here_task(prompt))
        timer_start = time.perf_counter()

        # self.vendors_results.append(
        #     obj
        # )
        results = await asyncio.gather(*tasks)
        timer_stop = time.perf_counter()
        if self.debug:
            print(f"Performed all prompts on {self.compared_vendors}... {timer_stop - timer_start:0.4f} seconds")
        # print('results', results)
        # print('self.vendors_results', self.vendors_results)
        count = 0
        if len(self.compared_vendors):
            for idx in range(0, len(results), len(self.compared_vendors)):
                if self.vendors_results[count]:
                    for i, vendor in enumerate(self.compared_vendors):
                        self.vendors_results[count][vendor] = results[idx + i]
                    # self.vendors_results[count]['took'] = f'{timer_stop - timer_start:0.4f}'
                    count += 1

    async def run(self, prompts: list):
        self.reset()
        self.timer_start = time.perf_counter()
        for item in prompts:
            await self.process_item(item)
        self.timer_end = time.perf_counter()
        self.total_took = self.timer_end - self.timer_start
