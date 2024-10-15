# -*- coding: utf-8 -*-
import os
import json
import re

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--not_processed_QA_chain_folder', type=str, required=True, help='the path of folder you save QA chains without right format')
parser.add_argument('--output_folder', type=str, required=True, help='the path of folder you want to save QA chains with right format')

args = parser.parse_args()

input_json_path = args.not_processed_QA_chain_folder
output_folder = args.output_folder

def process_and_save_json(input_json_path):

    json_names = os.listdir(input_json_path)
    for json_name in json_names:
        save_name = json_name.split('.')[0]
        print(save_name)
        json_path = os.path.join(input_json_path,json_name)
        with open(json_path,'r') as file:
            datas = json.load(file)
        output = []
        for data in datas:
            text = data['answers']
            if text is None:
                output.append({})
            else:
                if text[0:3] == '```':
                    parts = text.split('```')
                    for part in parts:
                        if part[0:5] == 'json\n':
                            part = part.replace("json\n", "").replace("]\n\n",",").replace("\n","").replace("\\","").strip()
                            if part.startswith("{") and part.endswith("}"):
                                part = part[1:-1].strip()
                                if part.startswith("{") and part.endswith("}"):
                                    part = part
                                else:
                                    part = '{' + part + '}'
                            else:
                                part = part[1:-1].strip()
                            partJson = json.loads(part)
                else:
                    partJson = json.loads(text)
                outputData = {
                    "images":data['images'],
                    "chain":partJson,
                    "qac_timestamps_start":data['start_time'],
                    "qac_timestamps_end":data['end_time'],
                }
                output.append(outputData)
        with open(output_folder + '/' + save_name + '.json', 'w') as json_file:
            json.dump(output, json_file, ensure_ascii=False, indent=4)

process_and_save_json(input_json_path)