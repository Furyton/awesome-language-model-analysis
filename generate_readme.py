import os
import csv

ROOT = "papers"
FILE_NAME = "papers.csv"
TEMPLATE_NAME = "README.template"

directory = [
    "phenomena-of-interest/in-context-learning",
    "phenomena-of-interest/chain-of-thought",
    "phenomena-of-interest/hallucination",
    "phenomena-of-interest/reversal-curse",
    "phenomena-of-interest/scaling-laws",
    "phenomena-of-interest/knowledge",
    "phenomena-of-interest/training-dynamics",
    "phenomena-of-interest/learning",
    "phenomena-of-interest/other-phenomena",
    "representational-capacity/what-can-transformer-do",
    "representational-capacity/what-can-transformer-not-do",
    "architectural-effectivity/layer-normalization",
    "architectural-effectivity/tokenization",
    "training-paradigms",
    "mechanistic-engineering",
    "miscellanea",
]


TEMPLATE = """
- **{}** [[paper link]]({}) {}  
{}
"""


def get_section_list(topic):
    p = os.path.join(ROOT, topic, FILE_NAME)

    # read as dict, the first line is the header

    with open(p, "r") as f:
        reader = csv.DictReader(f)
        # sort by date
        reader = sorted(reader, key=lambda x: x["Date"], reverse=True)
        # sanity check of each row
        for row in reader:
            assert len(row.keys()) == 4, row
            for key in row.keys():
                assert key in ["Title", "Date", "Url", "Author"], row
        paper_list = [TEMPLATE.format(row["Title"], row["Url"], row["Date"], row["Author"]) for row in reader]

    paper_list = "\n\n".join(paper_list)

    return paper_list

def fill_readme_template(output_path, content_dict):
    template_path = os.path.join(ROOT, TEMPLATE_NAME)
    with open(template_path, 'r') as file:
        template_content = file.read()

    filled_content = template_content.format(**content_dict)

    with open(output_path, 'w') as file:
        file.write(filled_content)

if __name__ == "__main__":
    content_dict = {}

    for d in directory:
        content_dict[d] = get_section_list(d)

    fill_readme_template("README.md", content_dict)
