import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from textblob import TextBlob
from newspaper import Article

url = 'https://en.wikipedia.org/wiki/Crimson_Desert'

article = Article(url)

# 1. Fetch and clean the article
article.download()
article.parse()
article.nlp()

# 2. Display Article Details
print("=" * 50)
print(f"Title: {article.title}")
print(f"Authors: {', '.join(article.authors) if article.authors else 'Not specified'}")
print(f"Publication Date: {article.publish_date}")
print("=" * 50)
print(f"Summary:\n{article.summary}")
print("=" * 50)

# 3. Sentiment Analysis with TextBlob
# We analyze the summary (or article.text) to determine the emotion
analysis = TextBlob(article.summary)

polarity = analysis.sentiment.polarity
subjectivity = analysis.sentiment.subjectivity

print(f"Polarity Score: {polarity:.2f}  (-1.0 = Very Negative, +1.0 = Very Positive)")
print(f"Subjectivity Score: {subjectivity:.2f}  (0.0 = Very Objective, 1.0 = Very Opinionated)")

# 4. Interpret the Sentiment
if polarity > 0:
    sentiment_label = "Positive 😊"
elif polarity < 0:
    sentiment_label = "Negative 🙁"
else:
    sentiment_label = "Neutral 😐"

print(f"Overall Sentiment: {sentiment_label}")
print("=" * 50)