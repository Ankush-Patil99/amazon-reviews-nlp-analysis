"""
aspect_extraction.py
Simple keyword-based aspect extraction utilities.

Usage:
from src.aspect_extraction import extract_aspects_from_text, extract_aspects_series
"""
from typing import List
import pandas as pd

DEFAULT_ASPECTS = [
    "battery", "price", "quality", "delivery", "design",
    "performance", "service", "packaging", "screen", "camera",
    "sound", "battery life", "charger", "warranty"
]

def extract_aspects_from_text(text: str, aspects: List[str] = None) -> List[str]:
    """
    Keyword-based extraction:
    Returns list of aspects found in text (case-insensitive).
    """
    if aspects is None:
        aspects = DEFAULT_ASPECTS
    if not isinstance(text, str) or text == "":
        return []
    text_l = text.lower()
    found = []
    for asp in aspects:
        # allow multi-word aspect matching
        if asp in text_l:
            found.append(asp)
    return found

def extract_aspects_series(series: pd.Series, aspects: List[str] = None, sample_size: int = None) -> pd.Series:
    """
    Apply extraction to a pandas Series (cleaned text).
    Optionally use sample_size to speed up processing during development.
    Returns a Series of lists.
    """
    if sample_size is not None:
        series = series.sample(n=sample_size, random_state=42)
    return series.fillna("").apply(lambda x: extract_aspects_from_text(x, aspects))
