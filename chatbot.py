# Chatbot greets the user.
print("Hello! Welcome to AI ChatBot. When you want to exit the conversation, type 'bye'.")

# Take user input and convert to lower case
while True:
    user_input = input("User: ").lower()
    
    if user_input == "bye":
        print("ChatBot: Goodbye!")
        break
    elif "hello" in user_input:
        print("ChatBot: Hi there! How can I assist you today?")
    elif "how's it going" in user_input:
        print("ChatBot: I am great, how are you?")
    elif "what's up" in user_input:
        print("ChatBot: The ceiling.") 
    elif "what is your name" in user_input:
        print("ChatBot: I am ChatBot and here to assist you!")
    else:
        print("ChatBot: Sorry, I didn't get that.")

print("Chat ended.")
