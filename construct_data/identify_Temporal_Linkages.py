# -*- coding: utf-8 -*-
import os, sys
sys.path.append(".")
from clients.chatgpt_client import GPT
from glob import glob
import json
import math

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--QA_chains_folder', type=str, required=True, help='the path of folder you want to save QA chains annotated with right format')
parser.add_argument('--output_folder', type=str, required=True, help='the path of folder you want to save temporal linkages without right format')

args = parser.parse_args()

inputPath = args.QA_chains_folder
output_folder = args.output_folder

for root, dirs, files in os.walk(inputPath):
    for name in files:
        file_path = os.path.join(root, name)
        video_name, _ = os.path.splitext(name)
        with open(file_path, 'r', encoding='utf-8') as file:
            datas = json.load(file)

        prompt_template = """
        Task Description:
        You are given two QA chains, each consisting of 5-6 consecutive open-ended question and answer pairs, generated for two different but connected segments of the same video. Your task is to find the related QA pairs between the two chains.

        Generated Example:
        {{
            "questionsBefore": [
                "What kind of gear are the racers wearing?",
                "What kind of gear are the racers wearing?",
                "What are they preparing to do?",
                "How many contestants are there in total?",
                "What is the scene like where they are?",
                "What happened at the start of the race?",
                ...
            ],
            "answersBefore": [
                "The racers are wearing motocross suits and helmets.",
                "The racers are wearing motocross suits and helmets.",
                "They are preparing to start the race.",
                "There are more than ten contestants in total.",
                "They are waiting behind the starting line on the race track.",
                "They started rushing down the hill.",
                ...
            ],
            "questionsAfter": [
                "What kind of clothing are the racers wearing?",
                "What kind of clothing are the racers wearing?",
                "What were the racers doing at the start of the race?",
                "What is the scene like now?",
                "How many people jumped over the ramp?",
                "What happened next?",
                ...
            ],
            "answersAfter": [
                "The racers are wearing racing suits of various colors, most equipped with safety helmets.",
                "The racers are wearing racing suits of various colors, most equipped with safety helmets.",
                "The racers are rushing down the hill, preparing to jump.",
                "They just rushed down the hill and are now at the bottom, about to jump over the ramp.",
                "Four contestants were the first to jump over the ramp.",
                "A contestant jumped over the ramp.",
                ...
            ],
            "relationship":[
                "People",
                "Objects",
                "Actions",
                "Environment",
                "Quantity",
                "Events",
                ...
            ]
        }}

        Requirements for generating the QA chain:
        - Note that when looking for related QA pairs, you should look for connections in the following six aspects: connections between actions, i.e., when two QA pairs involve related actions; connections between quantities, i.e., when two QA pairs involve related numbers of people or objects; connections between people, i.e., when two QA pairs involve related people; connections between objects, i.e., when two QA pairs involve related objects; connections between events, i.e., when two QA pairs involve the same or related events and activities; connections between environments, i.e., when two QA pairs involve the same scene or changes in the scene.
        - Note that each input QA chain contains two key-value pairs: "questions" and "answers". "Questions" is a list of all the questions generated in a QA chain; "answers" is a list of all the answers generated in a QA chain.
        - Generate the result in the format provided in the example and output all results in JSON format without generating any additional content. The output should contain five key-value pairs: "questionsBefore" is a list of questions from the first QA chain that are related to the questions and answers in the second QA chain; "answersBefore" is a list of answers from the first QA chain that are related to the questions and answers in the second QA chain; "questionsAfter" is a list of questions from the second QA chain that are related to the questions and answers in the first QA chain; "answersAfter" is a list of answers from the second QA chain that are related to the questions and answers in the first QA chain; "relationship" is a list of the types of connections between the related QA pairs.
        - Note that the number of related QA pairs in the "questionsBefore" and "questionsAfter" lists should be consistent, and the number of connections in the "relationship" list should be consistent with the number of related QA pairs in the two QA chains.
        - Note that for the two QA chains, you should output at least six pairs of related QA pairs, each of which should meet one of the six types of connections mentioned above.

        The "relationship" list should only include the following connections:
        1. "Actions", when the related QA pairs involve connections between actions.
        2. "Quantity", when the related QA pairs involve connections between quantities.
        3. "People", when the related QA pairs involve connections between people.
        4. "Objects", when the related QA pairs involve connections between objects.
        5. "Events", when the related QA pairs involve connections between events.
        6. "Environment", when the related QA pairs involve connections between environments.

        First QA Chain:
        {chain_1}

        Second QA Chain:
        {chain_2}
        """

        output = []
        for i in range(0,len(datas)-1):

            if len(datas[i]) == 0 or len(datas[i+1]) == 0:
                if len(datas[i]) == 0 and len(datas[i+1]) == 0:
                    output_data = {
                    "chain_1": {},
                    "chain_2": {},
                    "relationship": {}
                }
                elif len(datas[i]) == 0:
                    output_data = {
                    "chain_1": {},
                    "chain_2": {
                        "questions":datas[i+1]['chain']['questions'],
                        "answers":datas[i+1]['chain']['answers'],
                        'qac_timestamps_start':datas[i+1]['qac_timestamps_start'],
                        'qac_timestamps_end':datas[i+1]['qac_timestamps_end']
                    },
                    "relationship": {}
                }
                else:
                    output_data = {
                    "chain_1": {
                        "questions":datas[i]['chain']['questions'],
                        "answers":datas[i]['chain']['answers'],
                        'qac_timestamps_start':datas[i]['qac_timestamps_start'],
                        'qac_timestamps_end':datas[i]['qac_timestamps_end']
                    },
                    "chain_2": {},
                    "relationship": {}
                }
            else:
                prompt = prompt_template.format(chain_1=datas[i]['chain'],chain_2=datas[i+1]['chain'])

                gpt4v_client = GPT()

                answer = gpt4v_client.chat(prompt, max_cycle = 20)

                output_data = {
                    "chain_1": {
                        "questions":datas[i]['chain']['questions'],
                        "answers":datas[i]['chain']['answers'],
                        'qac_timestamps_start':datas[i]['qac_timestamps_start'],
                        'qac_timestamps_end':datas[i]['qac_timestamps_end']
                    },
                    "chain_2": {
                        "questions":datas[i+1]['chain']['questions'],
                        "answers":datas[i+1]['chain']['answers'],
                        'qac_timestamps_start':datas[i+1]['qac_timestamps_start'],
                        'qac_timestamps_end':datas[i+1]['qac_timestamps_end']
                    },
                    "relationship": answer
                }

            output.append(output_data)

        json_filename = output_folder + '/' + video_name + '.json'

        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(output, json_file, ensure_ascii=False, indent=4)

        print(f"Data has been written to {json_filename}")