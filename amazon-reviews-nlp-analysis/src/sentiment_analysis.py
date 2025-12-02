"""
sentiment_analysis.py
Lightweight sentiment utilities using TextBlob (rule-based).
Also includes simple label conversion helpers.

Usage:
from src.sentiment_analysis import get_polarity, label_sentiment
"""
from textblob import TextBlob
from typing import Optional

def get_polarity(text: str) -> Optional[float]:
    """
    Returns polarity float in [-1, 1]. Returns None for invalid input.
    Note: TextBlob is lightweight and deterministic; used for analysis (not SOTA).
    """
    if not isinstance(text, str) or text.strip() == "":
        return None
    try:
        return TextBlob(text).sentiment.polarity
    except Exception:
        return None

def label_sentiment(score: float, pos_thresh: float = 0.1, neg_thresh: float = -0.1) -> str:
    """
    Convert polarity score to label: Positive / Neutral / Negative
    """
    if score is None:
        return "Unknown"
    if score > pos_thresh:
        return "Positive"
    if score < neg_thresh:
        return "Negative"
    return "Neutral"
