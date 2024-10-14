# -*- coding: utf-8 -*-
import os, sys
sys.path.append(".")
from clients.chatgpt_client import GPT
from glob import glob
import json
import math
import re

def create_evaluation_prompt(video_id, scene_id, question_id, question, ground_truth, model_response):
    prompt = f"""
    Video ID: {video_id}
    Scene ID: {scene_id}
    Question ID:{question_id}

    Task Description:
    You are an expert judge evaluating the accuracy of answers to question about scenes in a streaming video. For each scene, there is a specific question and its ground truth answer. Several models have provided responses to these questions. Your task is to evaluate the accuracy of each response on a scale from 0 to 10, where:    
    
    - 10: The response is completely accurate and matches the ground truth in all relevant details, providing any necessary context.
    - 8-9: The response is mostly accurate but may miss minor details or context.
    - 6-7: The response is somewhat accurate but lacks significant details or context.
    - 4-5: The response provides some relevant information but misses key aspects of the ground truth.
    - 2-3: The response has little relevance or severely misconstrues the ground truth.
    - 0-1: The response is completely inaccurate or off-topic.

    Additional Requirements and Considerations for the Evaluator:
    1. Thoroughly Understand the Question: Ensure that you fully grasp the context and nuances of the question before evaluating the response.
    2. Accurate Comparison: Compare the model's response against the ground truth answer with a high degree of precision. Pay attention to the correctness, completeness, and relevance of the information provided.
    3. Objective Scoring: Assign a score on a scale from 1 to 10, focusing solely on the accuracy of the response. Do not consider style, grammar, or additional information that is unrelated to accuracy.
    4. Detailed Explanation: Provide a clear and concise explanation for the score you assign. This explanation should justify your scoring by pointing out specific accurate or inaccurate details in the model's response.
    5. Consistency: Apply the same criteria uniformly across all evaluations to ensure fairness and consistency in scoring.
    6. Be Neutral and Unbiased: Do not let any prior knowledge, assumptions, or personal opinions affect your judgment. Only use the provided ground truth and the response when making your decision.

    For the following QA, please evaluate the model's performance according to the criteria mentioned above and provide a detailed justification for each score.

    Questions:
    {question}
    
    Ground Truth:
    {ground_truth}

    Model Responses:
    {model_response}

    Please provide your evaluation scores and detailed comments for each criterion below:

    Accuracy:
    Score: 
    Comments:
    """

    return prompt

def extract_scores(evaluation, j):
    patterns = {
        "Accuracy": r'Accuracy.*\n?.*?Score.*?(\d+)'
    }
    
    scores = {category: None for category in patterns.keys()}
    
    for category, pattern in patterns.items():
        match = re.search(pattern, evaluation, re.DOTALL)
        if match:
            score = match.group(1)
            try:
                scores[category] = int(score)
                print(f"{category} Score: {score}")
            except ValueError:
                print(f"Failed to convert {category} Score: {score} to an integer.")
        else:
            print(f"{category} Score not found.")
    
    return scores

answers_path = 'Path_to_your_answer_dir'

for root, dirs, files in os.walk(answers_path):
    for name in files:
        file_path = os.path.join(root, name)
        video_name, _ = os.path.splitext(name)
        with open(file_path, 'r', encoding='utf-8') as file:
            datas = json.load(file)

        output = []
        gpt_client = GPT()

        for i in range(len(datas)):
            if len(datas[i]) == 0:
                continue
            
            question_chain = datas[i]['questions']
            ground_truth_chain = datas[i]['gt_answers']
            model_responses_chain = datas[i]['answers']

            scores = []

            for j in range(len(question_chain)):

                question_evaluation = {}

                prompt = create_evaluation_prompt(video_id=video_name, scene_id=i, question_id = j, question = question_chain[j], ground_truth = ground_truth_chain[j], model_response = model_responses_chain[j])
                print(f"Generated Prompt for video: {video_name}, scene: {i}, question: {j}")
                print(prompt)

                evaluation = ""
                while True:  
                    evaluation = gpt_client.chat(prompt)
                    if evaluation:
                        break
                    else:
                        print(f"Retrying evaluation for video: {video_name}, scene: {i}, question: {j}")
                
                print(f"GPT-4 Evaluation for video: {video_name}, scene: {i}, question: {j}")
                print(evaluation)

                question_scores = extract_scores(evaluation, j)
                
                question_evaluation = {
                    "question_id": j,
                    "question": question_chain[j],
                    "gt_answer": ground_truth_chain[j],
                    "model_response": model_responses_chain[j],
                    "evaluation": evaluation,
                    "question_scores": question_scores
                }
                
                scores.append(question_evaluation)

            output_data = {
                "video_name": video_name,
                "scene_id": i,
                "scores": scores
            }
            output.append(output_data)

        eval_SingleQA_result = f'Path_to_your_save_file'
        with open(eval_SingleQA_result, 'w', encoding='utf-8') as json_file:
            json.dump(output, json_file, ensure_ascii=False, indent=4)

        print(f"Data has been written to {eval_SingleQA_result}")



