"""
importance_scoring.py
Compute aspect importance and pain-point scores.

Usage:
from src.importance_scoring import compute_aspect_importance
"""
import pandas as pd
from typing import Tuple

def compute_aspect_importance(aspect_summary: pd.DataFrame, aspect_frequency: pd.DataFrame) -> pd.DataFrame:
    """
    aspect_summary: dataframe with columns ['aspects', 'aspect_sentiment'] (mean polarity per aspect)
    aspect_frequency: dataframe with columns ['aspect', 'frequency']
    Returns dataframe sorted by importance_score (desc) with columns:
      ['aspects', 'aspect_sentiment', 'frequency', 'importance_score']
    Importance = frequency * abs(mean_sentiment)
    """
    # rename to merge safely
    a_sum = aspect_summary.rename(columns={ 'aspects': 'aspect', 'aspect_sentiment': 'avg_sentiment' }).copy()
    a_freq = aspect_frequency.rename(columns={ 'aspect': 'aspect', 'frequency': 'frequency' }).copy()

    merged = pd.merge(a_sum, a_freq, on='aspect', how='inner')
    merged['importance_score'] = merged['frequency'] * merged['avg_sentiment'].abs()
    merged = merged.sort_values('importance_score', ascending=False).reset_index(drop=True)
    # rename columns back to expected names if desired
    merged = merged.rename(columns={'aspect': 'aspects', 'avg_sentiment': 'aspect_sentiment'})
    return merged[['aspects', 'frequency', 'aspect_sentiment', 'importance_score']]

def compute_pain_point_score(df_aspect_distribution: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame (aspects x sentiment_label counts) where negative counts exist,
    compute a simple 'pain_point_score' = frequency * (-average_negative_sentiment).
    This function is left generic; usage depends on how you structure input.
    """
    # Implementers can adapt to their distribution format.
    raise NotImplementedError("Use compute_aspect_importance for the standard importance score.")
