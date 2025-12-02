# 📘 Amazon Reviews NLP Analysis Project

## 🧠 Introduction
This project presents a complete end-to-end **Natural Language Processing (NLP)** workflow for analyzing Amazon product reviews.  
The goal is to extract meaningful customer insights through:
- Aspect extraction  
- Aspect-based sentiment analysis  
- Aspect importance scoring  
- Topic modeling  
- Transformer-based summarization (BART & T5)  
- Visual data storytelling  

This repository is structured professionally with modular Python scripts, notebooks, outputs, and documentation, making it suitable for real-world ML/NLP workflows and showcasing strong project engineering skills.

---

## 📂 Project Structure

Below is the complete folder structure for this project.  
Click to expand each section and access individual files.

---
<details>
<summary><strong>📁 data/processed</strong></summary>

| File | Description | Link |
|------|-------------|------|
| amazon_nlp_project_results.csv | (Not uploaded / Large file excluded) | — |
| aspect_importance_scores.csv | Aspect ranking with importance score | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/data/processed/aspect_importance_scores.csv) |
| aspect_sentiment_distribution.csv | Sentiment label distribution per aspect | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/data/processed/aspect_sentiment_distribution.csv) |
| aspect_sentiment_summary.csv | Average sentiment per aspect | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/data/processed/aspect_sentiment_summary.csv) |
| review_aspect_sentiment.csv | Aspect + sentiment per review | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/data/processed/review_aspect_sentiment.csv) |
| review_summarization_samples.csv | BART & T5 summaries for sample reviews | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/data/processed/review_summarization_samples.csv) |
</details>

---

<details>
<summary><strong>📁 notebooks</strong></summary>

| Notebook | Description | Link |
|----------|-------------|------|
| amazon-sentiment-nlp.ipynb | Main project notebook with full pipeline | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/notebooks/amazon-sentiment-nlp.ipynb) |

</details>

---

<details>
<summary><strong>📁 outputs/figures</strong></summary>

| Figure | Description | Link |
|--------|-------------|------|
| aspect_frequency.png | Aspect count distribution | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/outputs/figures/aspect_frequency.png) |
| aspect_importance.png | Aspect importance score visualization | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/outputs/figures/aspect_importance.png) |
| aspect_sentiment.png | Average sentiment per aspect | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/outputs/figures/aspect_sentiment.png) |
| review_length.png | Review length distribution | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/outputs/figures/review_length.png) |
| sentiment_polarity.png | Sentiment polarity histogram | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/outputs/figures/sentiment_polarity.png) |
| wordclouds.png | Wordcloud of reviews | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/outputs/figures/wordclouds.png) |

</details>

---

<details>
<summary><strong>📁 src (Python Modules)</strong></summary>

| Script | Description | Link |
|--------|-------------|------|
| preprocessing.py | Cleaning, tokenization, stopword removal utilities | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/src/preprocessing.py) |
| aspect_extraction.py | Keyword-based aspect mining logic | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/src/aspect_extraction.py) |
| sentiment_analysis.py | Polarity scoring + sentiment labeling | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/src/sentiment_analysis.py) |
| importance_scoring.py | Computes aspect importance using freq × sentiment | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/src/importance_scoring.py) |
| summarization.py | BART & T5 summarization utilities | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/src/summarization.py) |
| visualization.py | Wordcloud + graph saving functions | [Click Here](https://github.com/Ankush-Patil99/amazon-reviews-nlp-analysis/blob/main/amazon-reviews-nlp-analysis/src/visualization.py) |

</details>

---


---

## 🛠️ Key Features

### ✔ Text Preprocessing
- Tokenization  
- Lemmatization  
- Stopword removal  
- Cleaning & normalization  

### ✔ Aspect Extraction
- Keyword-based detection  
- Clean and optimized extraction logic  

### ✔ Aspect-Based Sentiment Analysis
- Rule-based polarity scoring using TextBlob  
- Aspect-level polarity and ranking  

### ✔ Aspect Importance Scoring
A key business insight metric:  
```
importance = frequency × |average sentiment|
```
Shows which features matter the most to customers.

### ✔ Topic Modeling
- Latent Dirichlet Allocation (LDA) for theme extraction  

### ✔ Transformer-Based Summarization
- BART for concise summaries  
- T5 for structured summarization  

### ✔ Data Visualizations
- Wordcloud  
- Sentiment histogram  
- Aspect sentiment bar charts  
- Aspect importance graph  

All visual outputs are stored under `outputs/figures/`.

---

## ▶️ How to Run the Project

### **1. Clone the Repository**
```
git clone https://github.com/YOUR-USERNAME/amazon-reviews-nlp-analysis.git
cd amazon-reviews-nlp-analysis
```

### **2. Install Dependencies**
```
pip install -r requirements.txt
```

### **3. Run Notebook**
Open:
```
notebooks/amazon-sentiment-nlp.ipynb
```

### **4. Use Modular Scripts (Optional)**
Example:
```python
from src.preprocessing import clean_text, fast_tokenize
from src.aspect_extraction import extract_aspects_from_text
```

---

## 📊 Results Overview

### ⭐ Aspect Importance
Identifies which aspects customers care about most.

### ⭐ Aspect Sentiment Summary
Aggregates positivity/negativity for each feature.

### ⭐ Summarization
Both BART & T5 models provide compact summaries of long reviews.

### ⭐ Final Outputs
Stored under:
```
data/processed/
```

---

## 🚀 Future Improvements
- Deploy as an API using FastAPI  
- Add sentiment classification model (BERT)  
- Build an interactive dashboard  
- Add named entity recognition (NER)  

---

## 👤 Author
**Ankush Patil**  
Machine Learning & NLP Engineer  
- LinkedIn: https://www.linkedin.com/in/YOUR-LINK  
- Email: your.email@example.com  
