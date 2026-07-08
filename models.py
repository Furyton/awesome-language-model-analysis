"""Thin wrapper around an OpenAI-compatible chat completion endpoint.

Works with DeepSeek (default), OpenAI, or any other OpenAI-compatible proxy
by setting GPT_API_BASE / GPT_MODEL / GPT_KEY.
"""
import logging

from constant import GPT_MODEL, GPT_API_BASE, GPT_KEY


def get_response(prompt: str) -> str:
    if not GPT_KEY:
        raise RuntimeError(
            "GPT_KEY is not set -- add a DeepSeek/OpenAI-compatible API key "
            "as the GPT_KEY secret to enable classification."
        )

    from openai import OpenAI

    client = OpenAI(api_key=GPT_KEY, base_url=GPT_API_BASE)

    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    text = response.choices[0].message.content
    logging.debug(f"[{GPT_MODEL}] response: {text}")
    return text
