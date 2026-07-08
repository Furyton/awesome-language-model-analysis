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

This paper list only collects **theoretical** papers about language models, especially large language models (LLMs) and transformer-based architectures.

"Theoretical" means the paper's main contribution is a formal, mathematical, or rigorously analytical characterization of some property, behavior, or limitation of these models -- e.g. proofs, provable guarantees, generalization/approximation bounds, expressivity or capacity results, convergence analysis, information-theoretic arguments, statistical learning theory, PAC-style learnability results, or a formal/mechanistic account of a phenomenon (grokking, in-context learning, hallucination, scaling laws, etc.).

A paper still counts as theoretical even if it also runs experiments to validate or illustrate its theoretical claims -- that's normal and does not disqualify it. What disqualifies a paper is having **no formal/theoretical component at all**.

Classify this paper into one or two of the categories below if (and only if) it is theoretical as defined above and it studies phenomena, properties, training dynamics, or representational capacities of language models / transformers. Return the one or two category codes (e.g., '01., 02.'). If it does not qualify, return 'None'.

Return 'None' if the paper:
- is a purely empirical/observational study with no formal theoretical analysis (e.g. "we run experiments and observe X" with no proof, bound, or formal characterization)
- is a benchmark, survey, evaluation, or dataset paper with no theoretical contribution
- is about a downstream application (translation, security/attacks, federated learning, vision-language, retrieval, agents, robotics, etc.) rather than the model's own properties
- is about very specific downstream tasks (dialogue, RAG, conversation, etc.)
- mainly proposes a new architecture, pretraining objective, or fine-tuning strategy to improve performance, without theoretically analyzing *why* it works

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

Remember: this list is theoretical papers only. Return 'None' if the paper:
- is a purely empirical/observational study with no formal theoretical analysis
- is a benchmark, survey, evaluation, or dataset paper with no theoretical contribution
- is about a downstream application (translation, security/attacks, federated learning, vision-language, retrieval, agents, robotics, etc.) rather than the model's own properties
- is about very specific downstream tasks (dialogue, RAG, conversation, etc.)
- mainly proposes a new architecture, pretraining objective, or fine-tuning strategy to improve performance, without theoretically analyzing why it works

A paper that includes experiments supporting a theoretical claim still counts as theoretical -- don't reject it just for having an empirical section.

Please refer to the examples for each category to understand the scope of each category.

If the paper is a genuinely theoretical work on language models, attention mechanisms, or transformer architecture but doesn't fit any category above precisely, put it into {category_info[-1]['code']}, {category_info[-1]['name']}.
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
