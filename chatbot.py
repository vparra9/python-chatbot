# For random responses
import random 
#Import regex library
import re

# Chatbot greets the user.
print("Hello! Welcome to AI ChatBot. When you want to exit the conversation, type 'bye'.")

# Take user input and convert to lower case
while True:
    user_input = input("User: ").lower()
    
    if user_input == "bye":
        print("ChatBot: Goodbye!")
        break

    elif re.search(r"\bhello\b|\bhello\b|\bhey\b", user_input):
        print("ChatBot: Hi there! How can I assist you today?")
    elif re.search(r"how. *you", user_input):      #How are you, how's it going, etc
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
        responses = [
            "I do not understand, can you rephrase that?",
            "Sorry, I didn't get that."
            ]
        print(f"ChatBot: {random.choice(responses)}")

print("Chat ended.")
