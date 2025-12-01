# For random responses
import random 
#Import regex library
import re
import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import requests

# Download NLTK resources that are needed
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet") # For lemmatization

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english")) - {"are"}

API_KEY = "a804808772e57b1357ab2c921390649d" # API key from OpenWeatherMap 

# Gets weather information
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature_celsius = data['main']['temp']
        temperature_fahrenheit = (temperature_celsius * 9/5) + 32
        return f"The weather in {city.capitalize()} is currently {weather} with a temperature of {temperature_fahrenheit:.1f} fahrenheit."
    else:
        return "Sorry, the weather is not available for this city, please check the city name and try again."

# Chatbot greets the user.
print("Hello! Welcome to AI ChatBot. When you want to exit the conversation, type 'bye'.")

# Take user input and convert to lower case
while True:
    user_input = input("User: ").lower()
    
    if user_input == "bye":
        print("ChatBot: Goodbye!")
        break

    # Pattern matching
    if re.search(r"\bhello\b|\bhey\b|\bhi\b|\bgood morning\b|\bgood afternoon\b|\bgood evening\b", user_input):
        print("ChatBot: Hi there! How can I help you with your travel plans?")
    elif re.search(r"how.*are.*you", user_input):      #How are you, how's it going, etc
        print("ChatBot: I am great and ready to help you travel!") 
    elif re.search(r"what is your name", user_input):
        print("ChatBot: I am ChatBot and here to assist you with your travels!")
    elif re.search(r"what can you do", user_input):
        print("ChatBot: I can help you plan your trips, suggest destinations, and provide you with travel tips!")
    elif re.search(r"where are you from", user_input):
        print("ChatBot: I am from a special place called the internet. Data flows like a river here and every byte is an adveture!")
    elif re.search(r"i love traveling", user_input):
        print("ChatBot: That's fantastic! Where would you like to travel to?")
    elif re.search(r"where would you travel to", user_input):
        print("ChatBot: I think Paris would be a dream!")
    elif re.search(r"i'm excited to travel", user_input):
        print("ChatBot: That's great! Do you already have a trip planned?")
    elif re.search(r"i want to know more about traveling", user_input):
        print("ChatBot: Sure! What information are you looking for?")
    elif re.search(r"do you travel", user_input):
        print("ChatBot: I wish that I could, but I am stuck here in the digital world! Where would you like to go?")
    elif re.search(r"can you recommend a place to visit", user_input):
        print("ChatBot: Absolutely, what do you enjoy? Mountains, beach, or city life?")
    elif re.search(r"What travel tips do you have?", user_input):
        print("ChatBot: Always pack a toothbrush and keep your travel documents secure! What kind of tips are you looking for?")
    elif re.search(r"what do you like to do", user_input):
        print("ChatBot: I love helping others plan their adventure! What kind of activities do you enjoy while traveling?")
    elif re.search(r"how's the weather", user_input):
        city = input("ChatBot: Which city do you want to know the weather for?\nUser:")
        weather_info = get_weather(city)
        print(f"ChatBot: {weather_info}")

    elif re.search(r"fun fact", user_input):
        jokes = [
                "The world's longest commercial flight took around 30 hours.",
                "The shortest commercial flight takes less than two minutes",
                "India's train transport roughly 23 million passengers each day",
                "Saudia Arabia has no rivers",
                "It is the same time at both ends of China.",
                "The Great Wall of China is not in fact visible from space.",
                "Sudan has more ancient pyramids than Egypt.",
                "You're never more than 30 steps away from a trash can in Disneyland."
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
