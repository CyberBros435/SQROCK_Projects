# Phishing Email Detection with ML

Naive Bayes text classifier detecting phishing emails using scikit-learn, trained on a 50-sample labeled dataset (25 phishing, 25 legit).

## What It Does
Vectorizes email text (bag-of-words) → trains MultinomialNB → evaluates on held-out test split → predicts on new unseen emails.

## Tools
- scikit-learn (`CountVectorizer`, `MultinomialNB`, `Pipeline`)
- pandas

## Usage
```bash
pip install -r requirements.txt
python phishing_ml_classifier.py
```

## Theory
- NLP + ML can classify emails with 95%+ accuracy when trained on sufficient data
- Key features: keyword frequency, urgency language, "verify/click/claim" patterns
- Naive Bayes is fast and effective for text classification due to word-independence assumption working well in practice for spam/phishing detection

## Full Analysis
See [`report/report.md`](report/report.md) for dataset, confusion matrix, and accuracy report.