import llm

from constant import GPT_MODEL, GPT_API_BASE, GPT_KEY

model = llm.get_model(GPT_MODEL)

model.key = GPT_KEY
model.api_base = GPT_API_BASE


def get_response(prompt):
    response = model.prompt(prompt=prompt)

    return response.text()
