import os
import csv
import json
import random
import logging

from constant import ROOT
from models import get_response

with open("category_info.json", "r") as file:
    category_info = json.load(file)

category_info = sum([v["subcategories"] for v in category_info.values()], [])
code2category = {item["code"]: item for item in category_info}

PROMPT = """
Given the title and abstract of an arXiv paper:

Title: {}
Abstract: {}

Classify this paper into one or more of the following categories if it is about **theoretical or empirical analysis** of language models, especially large language models (LLMs) and transformer-based models. The categorization aims to understand different phenomena, properties, training dynamics, and representational capacities of these models.
Return the one or two category codes (e.g., '01., 02.') that best describe the paper. If the paper does not fall into any category, return 'None'.

Please ignore (return 'None') if this papers is not about theoretical analysis of language model.
Please ignore (return 'None') if this papers is about downstream or other applications of language models, e.g., translation, attack, security, federated learning, vision-language, etc.
Please ignore (return 'None') if this papers is about very specific downstream tasks, such as diaglue, rag, conversation, etc.
Please return 'None' if this paper focuses on improving the performance of language models, such as those that propose new architectures, pretraining objectives, or fine-tuning strategies.
Please only classify this paper if it mainly focuses on analyzing the theoretical properties of language models, especially large language models (LLMs), attention mechanism, or transformer architecture, etc.

Categories:\n
"""


def get_examples(category_code):
    # read the csv file and sample 2~3 the examples with random seed 13
    examples = []
    paper_path = os.path.join(
        ROOT, code2category[category_code]["directory"], "papers.csv"
    )

    with open(paper_path, "r") as file:
        reader = csv.DictReader(file)
        examples = [row["Title"] for row in reader]

    random.seed(13)
    random.shuffle(examples)

    return examples[:2]


for category in category_info:
    PROMPT += f"{category['code']}. **{category['name']}**: {category['description']}\n"

    examples = get_examples(category["code"])

    EXAMPLE = "Example of this category:\n"
    EXAMPLE += "\n".join([f"  - {example}" for example in examples])

    PROMPT += EXAMPLE + "\n\n"

PROMPT += f"""
---
Return the one or two category codes (e.g., '01., 02.') that best describe the paper.

If the paper does not fall into any category, return 'None'.

Please ignore (return 'None') if this papers is not about theoretical analysis of language model.
Please ignore (return 'None') if this papers is about downstream or other applications of language models, e.g., translation, attack, security, federated learning, vision-language, etc.
Please ignore (return 'None') if this papers is about very specific downstream tasks, such as diaglue, rag, conversation, etc.
Please return 'None' if this paper focuses on improving the performance of language models, such as those that propose new architectures, pretraining objectives, or fine-tuning strategies.
Please only classify this paper if it mainly focuses on analyzing the theoretical properties of language models, especially large language models (LLMs), attention mechanism, or transformer architecture, etc.

Please refer to the examples for each category to understand the scope of each category.

If the paper is a theoretical work on language model, attention mechanism, or transformer architecture, please return the corresponding category code(s) or put it into {category_info[-1]['code']}, {category_info[-1]['name']} if you are not sure.
"""


def categorize_paper(title, abstract):
    prompt = PROMPT.format(title, abstract)

    # Invoke the LLM to get the response
    response = get_response(prompt)

    logging.debug(f"Response for {title}:\n{response}")

    # Extract the category names from the response
    matched_categories = []

    for code, category in code2category.items():
        if code in response:
            matched_categories.append(category)

    logging.debug(f"Matched categories: {matched_categories}")

    # If no categories were matched, return 'None'
    if not matched_categories:
        return None

    return matched_categories
