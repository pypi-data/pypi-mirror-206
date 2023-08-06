import asyncio
import csv
import json
from gaia.base.vendors.vendors_manager import VendorsManager
from gaia.base.vendors.chat_gpt import ChatGptService

class Gaia:
    debug=False
    api_token=None
    api_keys: dict = {}
    def __init__(self, api_token, api_keys={}, debug=False):
        self.api_token = api_token
        self.api_keys = api_keys
        self.debug = debug

    def optimize_prompt(self, prompt):
        # TODO run optimize prompt with chat gpt
        c = VendorsManager(debug=self.debug)
        start = '<'
        end = '>'
        param = prompt[prompt.find(start) + len(start):prompt.rfind(end)]
        p = f"please optimize this prompt to get better results for any {param}: {prompt}" \
            f", provide only the final suggested prompt"
        prediction = c.chatGptService.run_chat(p, [], False)
        text = prediction.choices[0].message.content
        return text

    def load_data(self, csv_path):
        csvfile = open(csv_path, 'r', encoding='utf-8')
        # print('csvfile', csvfile)
        csvReader = csv.DictReader(csvfile)
        # print('csvReader', csvReader)
        data = []
        for row in csvReader:
            clean_row = {}
            for k, v in row.items():
                if k:
                    clean_row[k] = ("" if v == None else v)
            # clean_row = {k: ("" if v == None else v) for k, v in row.items()}
            data.append(clean_row)
        return data

    def run_vendors(self, vendors=None, data=[]):
        c = VendorsManager(vendors=vendors, api_keys=self.api_keys, debug=self.debug)
        asyncio.run(c.run_all_parallel(data))
        data = {'vendors_results': c.vendors_results, 'total_took': c.total_took, 'compared_vendors': c.compared_vendors}
        return data

    def save_csv(self, csv_path=None, data=[]):
        csvfile = open(csv_path, 'w', encoding='utf-8', newline="")
        first_row = self.flatten_dict(data[0])
        headers = first_row.keys()
        writer = csv.DictWriter(csvfile,fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(self.flatten_dict(row))
        return csv_path

    def flatten_dict(self, dd, separator='_', prefix=''):
        return {prefix + separator + k if prefix else k: v
            for kk, vv in dd.items()
            for k, v in self.flatten_dict(vv, separator, kk).items()
            } if isinstance(dd, dict) else {prefix: dd}

    def get_available_vendors(self):
        return VendorsManager.available_vendors