import os
import json

ROOT = "papers"
PENDING_DIR = "papers/_pending"
PENDING_FILE = f"{PENDING_DIR}/queue.csv"
PENDING_FIELDS = ["Title", "Date", "Url", "Author", "Abstract", "Source"]

DOCS_DIR = "docs"
SITE_DATA_FILE = f"{DOCS_DIR}/data/papers.json"

if os.path.exists("debug_secret.json"):
    with open("debug_secret.json") as f:
        os.environ.update(json.load(f))


def _env(name, default=None):
    # GitHub Actions turns `env: X: ${{ secrets.X }}` into X="" when the
    # secret doesn't exist (not "unset"), so treat empty string as unset too
    # -- otherwise a missing optional secret silently overrides our default.
    value = os.environ.get(name)
    return value if value else default


# --- LLM classification (OpenAI-compatible; DeepSeek, OpenAI, etc.) ---
# DeepSeek default: GPT_API_BASE=https://api.deepseek.com, GPT_MODEL=deepseek-v4-flash
# (deepseek-v4-flash, non-thinking mode -- cheap, fine for this classification task.
# The older "deepseek-chat" alias is deprecated 2026-07-24.)
GPT_MODEL = _env("GPT_MODEL", "deepseek-v4-flash")
GPT_API_BASE = _env("GPT_API_BASE", "https://api.deepseek.com")
GPT_KEY = _env("GPT_KEY")  # required to actually classify; pending queue is used if absent

# --- Gmail IMAP (for parsing arxivist digest emails) ---
GMAIL_ADDRESS = _env("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = _env("GMAIL_APP_PASSWORD")
IMAP_HOST = _env("IMAP_HOST", "imap.gmail.com")

# --- Scholar Inbox: authenticated via the permanent magic-link sha_key
# (see fetch_scholar_inbox.py). This is a bearer credential for your
# account -- keep it a GitHub secret only, never commit it.
SCHOLAR_INBOX_SHA_KEY = _env("SCHOLAR_INBOX_SHA_KEY")

# --- arXiv search fallback / backfill ---
# This list only tracks *theoretical* papers now, so the search requires a
# hit from BOTH buckets below (LM/transformer subject matter AND a signal of
# theoretical/formal treatment) rather than one big OR list -- that single
# generic list used to pull in huge amounts of noise (any ML paper that
# mentions "language model" or "attention mechanism" in passing, e.g. drug
# design, forecasting, robotics papers). The final call is always the LLM
# classifier; this search just needs to not filter out real matches, so it
# errs generous on both buckets.
ARXIV_CATEGORIES = ["cs.CL", "cs.LG", "stat.ML"]

ARXIV_TOPIC_TERMS = [
    "language model",
    "large language model",
    "transformer",
    "attention mechanism",
    "self-attention",
    "in-context learning",
    "chain-of-thought",
    "chain of thought",
    "hallucination",
    "scaling law",
    "emergent ability",
    "grokking",
    "tokenization",
    "layer normalization",
    "memorization",
    "reversal curse",
    "state space model",
    "linear attention",
    "mixture of experts",
]

ARXIV_THEORY_TERMS = [
    "theoretical",
    "theoretically",
    "theory of",
    "a theory",
    "provable",
    "provably",
    "proof",
    "prove that",
    "we prove",
    "convergence",
    "generalization bound",
    "sample complexity",
    "expressivity",
    "expressive power",
    "approximation theory",
    "statistical learning theory",
    "learnability",
    "PAC learning",
    "information-theoretic",
    "VC dimension",
    "closed-form",
    "analytically",
    "upper bound",
    "lower bound",
    "bayesian",
    "probabilistic framework",
    "formal framework",
    "formal analysis",
    "mathematical framework",
    "mathematical model of",
    "characterize",
    "characterization",
    "guarantee",
]

# kept for backwards compatibility with any old references; not used in
# the query itself anymore
ARXIV_KEYWORDS = ARXIV_TOPIC_TERMS
