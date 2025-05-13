import nltk
from nltk.chat.util import Chat, reflections

# Predefined pairs of inputs and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created to chat with you!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "It's alright", "Don't worry about it"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Great!"]
    ],
    [
        r"(.*) age?",
        ["I'm just a few lines of code!"]
    ],
    [
        r"(.*) created you?",
        ["I was created by a Python programmer."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm in the cloud, everywhere and nowhere!"]
    ],
    [
        r"quit",
        ["Bye for now!", "It was nice talking to you. See you later!"]
    ]
]

# Create and start the chatbot
def chatbot():
    print("Hi! I'm ChatBot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
