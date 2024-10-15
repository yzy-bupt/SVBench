# -*- coding: utf-8 -*-
import os, sys
sys.path.append(".")
from clients.chatgpt_client import GPT
from glob import glob
import json
import math

import pandas as pd
import csv
import ast
from datetime import datetime, timedelta

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--video_meta_with_timestamp', type=str, required=True, help='the path of meta file of videos with video paths and timestamps')
parser.add_argument('--video_frame_folder', type=str, required=True, help='the path of the folder saving all the video frames')
parser.add_argument('--output_folder', type=str, required=True, help='the path of folder you want to save QA chains without right format')

args = parser.parse_args()

inputPath = args.video_meta_with_timestamp
video_frame_folder = args.video_frame_folder
output_folder = args.output_folder

prompt = """
    Task Description:
    Based on a series of video frames arranged in chronological order, construct a chain of 5-6 consecutive open-ended question and answer pairs. In the question and answer chain, except for the first question, the content of the other questions must continue from the answer to the previous question. It is allowed to ask vague questions such as "What is he doing?". If the previous question is not correctly answered, the current question cannot be answered. The content must not skip to anything other than the answer to the previous question.

    Generated QA Chain:
    {{
        "questions": [
            "Are there any other contestants who fell?",
            "How did he fall?",
            "What happened to the other contestant who fell?",
            "How does he look?",
            ...
        ],
        "answers": [
            "Another rider wearing red, white, and blue also fell.",
            "He tried to avoid the first person who fell but failed.",
            "The other contestant who fell ran off the track and sat on the side.",
            "He looks seriously injured.",
            ...
        ]
    }}

    Requirements for generating the QA chain:
    - Generate the QA chain in the format provided in the example and output the QA chain in JSON format without generating any additional content. The QA chain should contain two key-value pairs: "questions" and "answers". "Questions" is a list of all the questions generated in the QA chain; "answers" is a list of all the answers generated in the QA chain.
    - Ensure that the questions in the QA chain are open-ended and can explore multiple different angles of the video content, but should not overly focus on detailed content. Reasonable questions should be asked about the following: complex plot understanding, such as "What is the boy's motivation throughout the video?"; inference of implicit information, such as "How did the boy and girl in the video meet?"; analysis of emotional coherence, such as "At what moments in the video does the boy feel the happiest?"; understanding of complex actions, such as "How is this magic trick performed?"; association and memory of details, such as "What is the connection between the first scene and the last scene in the video?"; multi-level plot analysis, such as "What is the turning point of this plot?".
    - Ensure that the questions and answers in the QA chain are strictly based on the video content itself, constructed only from the direct information in the video, avoiding any unnecessary speculation or over-association.
    - Ensure that the questions in the QA chain are clear and specific, directly corresponding to specific information or events in the video, and can be directly answered by watching the video content without the need for video description assistance or inference. Avoid asking questions that require assumptions or reasoning.
    - Ensure that the questions and answers do not contain specific time descriptions such as "at the nth second".
    - Ensure that the QA does not contain information sources, avoiding phrases like "from the image", "image sequence", "nth frame", or "nth picture". The input should be understood as a video, and you can describe it using video scenes.
    """

with open(inputPath, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        video_path = row['path']
        scenes = ast.literal_eval(row['timestamp'])
        file_name = os.path.basename(video_path)
        video_name, _ = os.path.splitext(file_name)

        data = []

        for scene in scenes:

            gpt4v_client = GPT()

            image_paths = glob(video_frame_folder + '/' + video_name + "/*jpg")
            image_paths = sorted(image_paths)
            imagesFetched = []
            firstTime = datetime.strptime(scene[0], '%H:%M:%S.%f').hour * 3600 + datetime.strptime(scene[0], '%H:%M:%S.%f').minute * 60 + datetime.strptime(scene[0], '%H:%M:%S.%f').second + datetime.strptime(scene[0], '%H:%M:%S.%f').microsecond / 1e6
            secondTime = datetime.strptime(scene[1], '%H:%M:%S.%f').hour * 3600 + datetime.strptime(scene[1], '%H:%M:%S.%f').minute * 60 + datetime.strptime(scene[1], '%H:%M:%S.%f').second + datetime.strptime(scene[1], '%H:%M:%S.%f').microsecond / 1e6
            startSec = math.floor(firstTime)
            endSec = math.ceil(secondTime)
            if secondTime - firstTime < 1.5:
                continue
            if endSec - startSec + 1 > 10:
                step = (endSec - startSec)//9 + 1
                start = max(0, endSec - 9*step - 1)
                imagesFetched = image_paths[min(len(image_paths)-1,endSec):start:-step][::-1]
            else:
                imagesFetched = image_paths[startSec:endSec+1]
            answer = gpt4v_client.vision(prompt, imagesFetched, max_cycle = 20)

            while answer is None:
                answer = gpt4v_client.vision(prompt, imagesFetched, max_cycle = 20)

            output_data = {
                "images":imagesFetched,
                "answers": answer,
                "start_time": firstTime,
                "end_time": secondTime
            }

            pairJson = json.loads(json.dumps(output_data))
            data.append(pairJson)

        json_filename = output_folder + '/' + video_name + '.json'

        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        print(f"Data has been written to {json_filename}")