"""
preprocessing.py
Utility functions for cleaning and tokenizing review text.

Usage:
from src.preprocessing import clean_text, fast_tokenize, save_nltk_resources
"""
import re
from typing import List
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# lazy download helper
def save_nltk_resources():
    """Download NLTK resources used by this module. Call once (e.g., at notebook start)."""
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('punkt', quiet=True)

# initialize stopwords & lemmatizer after downloads
try:
    STOP_WORDS = set(stopwords.words('english'))
except Exception:
    # If NLTK resources not present, give friendly error if functions are used
    STOP_WORDS = set()
LEMMATIZER = WordNetLemmatizer()

def clean_text(text: str) -> str:
    """
    Basic, fast cleaning:
    - lowercases
    - removes urls, non-alpha chars
    - collapses whitespace
    """
    text = "" if text is None else str(text)
    text = text.lower()
    text = re.sub(r'http\S+', ' ', text)           # remove urls
    text = re.sub(r'[^a-z\s]', ' ', text)          # keep letters and spaces
    text = re.sub(r'\s+', ' ', text).strip()       # collapse whitespace
    return text

def fast_tokenize(text: str, lemmatize: bool = True, min_len: int = 3) -> List[str]:
    """
    Fast tokenization using str.split() (faster than nltk tokenize for large corpora).
    Removes stopwords, short tokens. Optionally lemmatizes.
    """
    if not isinstance(text, str) or text == "":
        return []
    words = text.split()
    if STOP_WORDS:
        words = [w for w in words if w not in STOP_WORDS and len(w) >= min_len]
    else:
        words = [w for w in words if len(w) >= min_len]
    if lemmatize:
        words = [LEMMATIZER.lemmatize(w) for w in words]
    return words
