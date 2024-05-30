responses = {
    "hello": "Hello!welcome to chatbot.",
    "thank you": " How can I assist you?",
    "how are you?": "I'm just a simple bot, but I'm doing great!",
    "who created you?":"I was created by a developer who loves Python",
    "do you have any favourite movie?":" I dont watch movies, but I hear 'the pursuit of happiness' is a good one!",
    "what is the unit for force?":"The unit for force in International System of units is Newton(N)",
    "thank you!":"Your Welcome! if you have any questions feel free to ask",

}


def get_response(user_input):
    user_input = user_input.lower()
    #error handling line if chatbot doesn't understand the question
    return responses.get(user_input, "I'm sorry, I don't understand that.")

# Main loop
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
 
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: " + responses["bye"])
            break
        response = get_response(user_input)
        print("Chatbot: " + response)


if __name__ == "__main__":
    chat()
