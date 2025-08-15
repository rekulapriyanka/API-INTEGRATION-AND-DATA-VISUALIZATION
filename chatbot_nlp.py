import nltk
import random
import datetime
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Responses for different intents
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Bye! Take care."],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "time": [f"The current time is {datetime.datetime.now().strftime('%H:%M')}."],
    "date": [f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}."],
    "weather": ["I can't check real-time weather yet, but it's always sunny in here 😄."],
    "fallback": ["Sorry, I didn't understand that. Can you rephrase?", "I'm not sure how to respond to that."]
}

# Keywords mapped to intents
keywords = {
    "greeting": ["hello", "hi", "hey", "greetings"],
    "goodbye": ["bye", "goodbye", "see you"],
    "thanks": ["thanks", "thank you"],
    "time": ["time", "clock"],
    "date": ["date", "day", "today"],
    "weather": ["weather", "rain", "sunny", "cloudy"]
}

# Preprocessing function
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

# Intent detection
def detect_intent(user_input):
    tokens = preprocess(user_input)
    for intent, keyword_list in keywords.items():
        for word in tokens:
            if word in keyword_list:
                return intent
    return "fallback"

# Main chatbot loop
def chatbot():
    print("🤖 Chatbot: Hello! Ask me anything or type 'bye' to exit.")
    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("🤖 Chatbot:", random.choice(responses["goodbye"]))
            break
        intent = detect_intent(user_input)
        print("🤖 Chatbot:", random.choice(responses[intent]))

if __name__ == "__main__":
    chatbot()