# TASK 1: CHATBOT WITH RULE BASED RESPONSES

import random
import re
import datetime

def simple_chatbot():
    """
    A simple chatbot with a wide range of pre-programmed responses,
    including a knowledge base, recommendations, and date/time functions.
    """
    # Lists for randomized responses
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a fake noodle? An Impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she should embrace her mistakes. She gave me a hug.",
        "Why can't a bicycle stand up by itself? It's two tired."
    ]
    
    recommendations = {
        "book": ["'Dune' by Frank Herbert", "'Project Hail Mary' by Andy Weir", "'The Hobbit' by J.R.R. Tolkien"],
        "movie": ["'Blade Runner 2049'", "'Interstellar'", "'The Matrix'"]
    }

    # A simple dictionary to act as a knowledge base
    knowledge_base = {
        "what is the capital of India": "The capital of India is New Delhi.",
        "who created python": "Python was created by Guido van Rossum in the late 1980s.",
        "what is the tallest mountain": "Mount Everest is the tallest mountain in the world.",
        "what is ai": "Artificial Intelligence is a branch of computer science dealing with the simulation of intelligent behavior in computers."
    }

    print("🤖 Hello! I am a Simple Chatbot. Feel free to ask me questions .")
    print("   You can ask for the time, a book recommendation, or a fun fact.")
    print("   Type 'bye' to exit.")
    print("-" * 60)

    while True:
        user_input = input("You: ").lower().strip()

        # --- Core Rules (Greetings & Farewells) ---
        if user_input in ["hello", "hi", "hey", "hola"]:
            print("Chatbot: Hello! Good to see you. What's on your mind?")
            continue
        
        if user_input in ["bye", "exit", "quit", "goodbye"]:
            print("Chatbot: It was nice chatting with you. Goodbye!")
            break

        # --- Personality & Interaction Rules ---
        if "how are you" in user_input:
            print("Chatbot: I'm a set of algorithms, so I'm always running at 100%! How about you?")
        elif "i am feeling" in user_input or "i'm feeling" in user_input:
            if "sad" in user_input or "down" in user_input:
                print("Chatbot: I'm sorry to hear that. I hope things look up for you soon.")
            elif "happy" in user_input or "great" in user_input:
                print("Chatbot: That's wonderful to hear! I'm glad you're having a good day.")
            else:
                print("Chatbot: Thanks for sharing. I'm here to listen.")
        elif "you are" in user_input and ("smart" in user_input or "clever" in user_input or "helpful" in user_input):
            print("Chatbot: Thank you! I do my best with the information I have.")
        elif "joke" in user_input:
            print(f"Chatbot: Here's one for you: {random.choice(jokes)}")
        
        # --- Utility & Knowledge Rules ---
        elif "time" in user_input or "date" in user_input:
            now = datetime.datetime.now()
            if "date" in user_input:
                print(f"Chatbot: Today's date is {now.strftime('%A, %B %d, %Y')}.")
            else:
                print(f"Chatbot: The current time is {now.strftime('%I:%M %p')}.")
        elif "calculate" in user_input or "what is" in user_input and re.search(r'\d', user_input):
            match = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', user_input)
            if match:
                num1, op, num2 = int(match.group(1)), match.group(2), int(match.group(3))
                if op == '+': result = num1 + num2
                elif op == '-': result = num1 - num2
                elif op == '*': result = num1 * num2
                elif op == '/': result = round(num1 / num2, 2) if num2 != 0 else "Error: Division by zero"
                print(f"Chatbot: The answer is {result}.")
            else:
                # Check if the query is in the knowledge base before giving up
                if user_input in knowledge_base:
                     print(f"Chatbot: {knowledge_base[user_input]}")
                else:
                     print("Chatbot: I can only do simple calculations like 'calculate 5 + 3'.")
        elif user_input in knowledge_base:
            print(f"Chatbot: {knowledge_base[user_input]}")
        elif "recommend" in user_input or "suggest" in user_input:
            if "book" in user_input:
                print(f"Chatbot: You should check out {random.choice(recommendations['book'])}.")
            elif "movie" in user_input:
                print(f"Chatbot: I've heard that {random.choice(recommendations['movie'])} is a great watch!")
            else:
                print("Chatbot: I can recommend a book or a movie. Which are you in the mood for?")
        elif "what can you do" in user_input or "help" in user_input:
            print("Chatbot: I can chat, tell jokes, do simple math, give recommendations, and share facts. What would you like to try?")

        # --- Default response ---
        else:
            print("Chatbot: That's an interesting thought. I don't have a pre-programmed response for that. Could you try rephrasing?")

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()