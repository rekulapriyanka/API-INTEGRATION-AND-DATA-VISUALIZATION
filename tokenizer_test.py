import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download only once; keeps it safe if it's missing
nltk.download('punkt')

# Your text
text = "Hello! This is a test. Let's see how it works."

# Tokenize sentences
sentences = sent_tokenize(text)
print("Sentences:", sentences)

# Tokenize words
words = word_tokenize(text)
print("Words:", words)
