# For random responses
import random 
#Import regex library
import re
import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources that are needed
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet") # For lemmatization

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english")) - {"are"}

# Chatbot greets the user.
print("Hello! Welcome to AI ChatBot. When you want to exit the conversation, type 'bye'.")

# Take user input and convert to lower case
while True:
    user_input = input("User: ").lower()
    
    if user_input == "bye":
        print("ChatBot: Goodbye!")
        break

    # Pattern matching
    if re.search(r"\bhello\b|\bhello\b|\bhey\b|\bhi\b", user_input):
        print("ChatBot: Hi there! How can I assist you today?")
    elif re.search(r"how.*are.*you", user_input):      #How are you, how's it going, etc
        print("ChatBot: I am great, how are you?")
    elif "what's up" in user_input:
        print("ChatBot: The ceiling.") 
    elif re.search(r"what is your name", user_input):
        print("ChatBot: I am ChatBot and here to assist you!")
    elif re.search(r"fun fact", user_input):
        jokes = [
                "Crocodiles can gallop like a horse.",
                "Nintendo is 130 years old",
                "A cloud weighs around a million tonnes",
                "Giraffes are 30 times more likely to get hit by lightning than people",
                "Identical twins do not have the same fingerprints",
                "Koalas have fingerprints"
                ]
        print(f"ChatBot: {random.choice(jokes)}")
    else:
        #Tokenization
        words = word_tokenize(user_input)
        #Remove stopwords and lemmatize words
        clean_words = {lemmatizer.lemmatize(word) for word in words if word not in stop_words}
        # Convert word to string to match
        cleaned_input = " ".join(clean_words)
        responses = [
            "I do not understand, can you rephrase that?",
            "Sorry, I didn't get that."
            ]
        print(f"ChatBot: {random.choice(responses)}")

print("Chat ended.")
