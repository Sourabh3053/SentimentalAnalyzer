# 📰 Article Sentiment Analyzer

An automated Python tool that extracts online articles and analyzes their emotional tone and subjectivity using Natural Language Processing (NLP).

---

## 🚀 Features

- **Automated Web Scraping:** Downloads web pages and removes ads, navigation menus, and HTML clutter using `newspaper3k`.
- **Text Summarization:** Generates a concise summary of the article using NLTK.
- **Sentiment Analysis:** Calculates emotional mood and objectivity using `TextBlob`:
  - **Polarity Score:** Measures how positive or negative the text is (`-1.0` to `+1.0`).
  - **Subjectivity Score:** Measures whether the text is fact-based or opinion-based (`0.0` to `1.0`).
- **Human-Readable Classification:** Labels the content as **Positive 😊**, **Negative 🙁**, or **Neutral 😐**.

---

## 🛠️ Built With

- **[Python 3](https://www.python.org/)**
- **[TextBlob](https://textblob.readthedocs.io/)** — Natural language processing and sentiment analysis.
- **[Newspaper3k](https://newspaper.readthedocs.io/)** — Article extraction and web scraping.
- **[NLTK](https://www.nltk.org/)** — Natural Language Toolkit for sentence tokenization.
- **[lxml_html_clean](https://pypi.org/project/lxml-html-clean/)** — HTML cleaning engine.

---

## 📦 Installation & Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/SentimentalAnalyzer.git
   cd SentimentalAnalyzer
   ```

2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script:**
   ```bash
   python SentimentalAnalyzer.py
   ```

---

## 📊 How to Understand the Results

| Metric | Range | Meaning |
| :--- | :--- | :--- |
| **Polarity** | `-1.0` to `+1.0` | **`-1.0`** = Highly Negative<br>**`0.0`** = Neutral<br>**`+1.0`** = Highly Positive |
| **Subjectivity** | `0.0` to `1.0` | **`0.0`** = Purely Factual (e.g. Wikipedia)<br>**`1.0`** = Pure Opinion (e.g. Personal Reviews) |

---

## 🖥️ Example Output

```text
==================================================
Title: Crimson Desert - Wikipedia
Authors: Not specified
Publication Date: None
==================================================
Summary:
Crimson Desert is an upcoming action-adventure game developed and published by Pearl Abyss...
==================================================
Polarity Score: 0.08  (-1.0 = Very Negative, +1.0 = Very Positive)
Subjectivity Score: 0.28  (0.0 = Very Objective, 1.0 = Very Opinionated)
Overall Sentiment: Positive 😊
==================================================
```

---

## 👤 Author
- **Sourabh Pahadi**
