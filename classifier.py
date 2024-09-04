import json
import logging

from models import get_response

with open("category_info.json", "r") as file:
    category_info = json.load(file)

category_info = sum([v["subcategories"] for v in category_info.values()], [])
code2category = {item["code"]: item for item in category_info}

PROMPT = """
Given the title and abstract of an arXiv paper:
Title: {}
Abstract: {}
Classify this paper into one or more of the following categories based on its focus on theoretical and empirical analysis of language models, especially large language models (LLMs), attention mechanism, or transformer-based models, etc. The categorization aims to understand different phenomena, properties, training dynamics, and representational capacities of these models.

Please ignore papers (return 'None') that focus on improving the performance, such as those that propose new methods.
Please select papers that mainly focus on analysing any **theoretical or empirical properties** of language model, attention mechanism, transformer, etc.

Categories:
"""

for category in category_info:
    PROMPT += f"{category['code']}. **{category['name']}**: {category['description']}\n"

PROMPT += "\nReturn the one or two category codes (e.g., '01., 02.') that best describe the paper. If the paper does not fall into any category, return 'None'.\nIf the paper is aiming at proposing new methods, please return 'None'.\nIf the paper is about analysing any **theoretical or empirical properties** of language model, attention mechanism, transformer, etc., please return the corresponding category code(s), or at least put them in the Miscellaneous category.\n\n"


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
