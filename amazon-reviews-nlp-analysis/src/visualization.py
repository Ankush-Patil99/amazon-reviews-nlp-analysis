"""
visualization.py
Helper plotting functions for saving charts used in the notebook.

Usage:
from src.visualization import save_wordcloud, save_bar_chart, save_hist
"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
from typing import List

def save_wordcloud(text: str, filename: str = "wordcloud.png", max_words: int = 200):
    wc = WordCloud(width=1600, height=800, background_color='white', max_words=max_words).generate(text)
    plt.figure(figsize=(12,6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

def save_bar_chart(x: List[str], y: List[float], filename: str = "bar_chart.png", title: str = "", xlabel: str = "", ylabel: str = ""):
    plt.figure(figsize=(10,5))
    plt.bar(x, y)
    plt.xticks(rotation=45, ha='right')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

def save_hist(values, filename: str = "hist.png", bins: int = 50, title: str = ""):
    plt.figure(figsize=(8,4))
    plt.hist(values, bins=bins)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
