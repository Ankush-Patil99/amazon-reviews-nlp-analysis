"""
summarization.py
Utilities for BART and T5 summarization using HuggingFace transformers.

Usage:
from src.summarization import load_bart_summarizer, bart_summarize, load_t5_model, t5_summarize
"""
from typing import List, Tuple
import torch

# ---- BART pipeline wrapper ----
def load_bart_summarizer(device: int = 0):
    """
    Loads huggingface pipeline for BART summarization.
    device: set to 0 for GPU, -1 for CPU
    Returns pipeline object.
    """
    try:
        from transformers import pipeline
    except Exception as e:
        raise RuntimeError("transformers not installed. pip install transformers") from e

    # device param: 0 -> first GPU, -1 -> CPU
    bart = pipeline("summarization", model="facebook/bart-large-cnn", device=device)
    return bart

def bart_summarize(pipeline_obj, texts: List[str], max_length: int = 70, min_length: int = 25) -> List[str]:
    """
    Summarize a list of texts using the provided pipeline object.
    """
    summaries = []
    for t in texts:
        if not isinstance(t, str) or t.strip() == "":
            summaries.append("")
            continue
        try:
            out = pipeline_obj(t, max_length=max_length, min_length=min_length, do_sample=False)
            summaries.append(out[0]['summary_text'])
        except Exception:
            summaries.append("")
    return summaries

# ---- T5 wrapper ----
def load_t5_model(device: str = "cuda"):
    """
    Loads t5-base tokenizer and model. Returns (tokenizer, model, device_str)
    device: "cuda" or "cpu"
    """
    try:
        from transformers import T5Tokenizer, T5ForConditionalGeneration
    except Exception as e:
        raise RuntimeError("transformers not installed. pip install transformers") from e

    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    if device == "cuda" and torch.cuda.is_available():
        model = model.to("cuda")
        dev = "cuda"
    else:
        dev = "cpu"
    return tokenizer, model, dev

def t5_summarize(tokenizer, model, text: str, device: str = "cuda", max_input_len: int = 512, max_length: int = 70, min_length: int = 25) -> str:
    """
    Summarize a single text using T5 tokenizer+model.
    """
    if not isinstance(text, str) or text.strip() == "":
        return ""
    if device == "cuda" and torch.cuda.is_available():
        device_str = "cuda"
    else:
        device_str = "cpu"
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=max_input_len, truncation=True)
    if device_str == "cuda":
        inputs = inputs.to("cuda")
        model = model.to("cuda")
    with torch.no_grad():
        summary_ids = model.generate(
            inputs,
            max_length=max_length,
            min_length=min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
