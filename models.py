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

    message = response.choices[0].message
    text = message.content

    if text is None:
        # Some DeepSeek models put output in reasoning_content instead of
        # content under certain finish reasons -- fall back rather than
        # silently returning None (which would blow up downstream string
        # matching with a confusing TypeError).
        text = getattr(message, "reasoning_content", None)
        if text is None:
            finish_reason = response.choices[0].finish_reason
            raise RuntimeError(
                f"Empty response from {GPT_MODEL} (finish_reason={finish_reason})"
            )

    # use repr() so a genuinely empty/None response is visually distinct
    # from the model literally answering the word "None"
    logging.debug(f"[{GPT_MODEL}] response: {text!r}")
    return text
