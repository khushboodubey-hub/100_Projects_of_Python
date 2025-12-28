import datetime
import random
import pyjokes

def chatbot():
    print("Chatbot: Hello! I am your dynamic chatbot 🤖. Type 'bye' to exit.\n")

    # Dynamic response lists
    greetings = ["Hello! 😊", "Hi there!", "Hey! What's up?", "Namaste! 🙏"]
    mood_responses = ["I'm great, thank you! 💖", "Doing awesome! What about you?", "I'm fine! Thanks for asking 😊"]
    thanks_responses = ["You're welcome! 😊", "Anything for you!", "No problem!"]
    compliments = [
        "You're doing amazing! Keep going! 🌟",
        "You’re smarter than you think 😉",
        "You're truly awesome! 😎"
    ]

    while True:
        user = input("You: ").lower()

        # Exit
        if "bye" or "byy" or "goodbye" in user:
            print("Chatbot: Goodbye Dear! Take care ❤️")
            break
                                                                                                                                   
        # Greetings
        elif any(word in user for word in ["hello", "hi", "hey", "namaste"]):
            print("Chatbot:", random.choice(greetings))

        # Mood check
        elif "how are you" in user:
            print("Chatbot:", random.choice(mood_responses))

        # User feels fine
        elif "i am fine" in user:
            print("Chatbot: That's awesome! 😄")

        # Name
        elif "your name" in user:
            print("Chatbot: I’m your dynamic Python chatbot!")

        # Time
        elif "time" in user:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print("Chatbot: The current time is", now)

        # Date
        elif "date" in user:
            today = datetime.date.today()
            print("Chatbot: Today's date is", today)

        # Thank you
        elif "thank" in user:
            print("Chatbot:", random.choice(thanks_responses))

        # Joke using pyjokes
        elif "joke" in user:
            joke = pyjokes.get_joke()  # Fetch a random funny joke
            print("Chatbot:", joke)

        # Compliment
        elif "compliment" in user:
            print("Chatbot:", random.choice(compliments))

        # Advice
        elif "advice" in user:
            print("Chatbot: Believe in yourself Dear. You’re stronger than you think ❤️")

        # Unknown
        else:
            print("Chatbot: Hmm... I didn't understand that. Try something else!")

# Run chatbot
chatbot()
