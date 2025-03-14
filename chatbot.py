# For random responses
import random 

# Chatbot greets the user.
print("Hello! Welcome to AI ChatBot. When you want to exit the conversation, type 'bye'.")

# Take user input and convert to lower case
while True:
    user_input = input("User: ").lower()
    
    if user_input == "bye":
        print("ChatBot: Goodbye!")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("ChatBot: Hi there! How can I assist you today?")
    elif "how's it going" in user_input or "how are you" in user_input:
        print("ChatBot: I am great, how are you?")
    elif "what's up" in user_input:
        print("ChatBot: The ceiling.") 
    elif "what is your name" in user_input:
        print("ChatBot: I am ChatBot and here to assist you!")
    elif "fun fact" in user_input:
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
