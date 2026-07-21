"""
Project 1: Rule-Based AI Chatbot
DecodeLabs - AI Engineering Internship (Batch 2026)

Goal:
    Create a simple rule-based chatbot that responds to predefined
    user inputs using if-else / dictionary logic, running in a
    continuous loop until the user exits.

Key Requirements met:
    - Handles greetings and exit commands
    - Uses if-else / dictionary-lookup logic for responses
    - Runs in a continuous loop (the "heartbeat")
    - Input sanitization (lower-case + strip whitespace)
    - Knowledge base with 5+ intents (dictionary, O(1) lookup)
    - Fallback response for unrecognized input
    - Clean exit strategy ("kill command")

Author: Irsa (FA23-BCS-111), COMSATS University Islamabad - Vehari Campus
"""

import random
import string
from datetime import datetime

# ---------------------------------------------------------------------------
# PHASE 1: KNOWLEDGE BASE
# Instead of a long, fragile if-elif ladder (O(n), high technical debt),
# we use a dictionary for O(1) constant-time lookup. Each key maps to a
# list of possible responses so the bot doesn't sound too robotic/repetitive.
# ---------------------------------------------------------------------------
KNOWLEDGE_BASE = {
    "hello": [
        "Hi there! How can I help you today?",
        "Hello! What can I do for you?",
    ],
    "hi": [
        "Hey! Good to see you.",
        "Hi! How's it going?",
    ],
    "how are you": [
        "I'm just a bunch of if-else logic, but I'm doing great! And you?",
        "Running smoothly, thanks for asking!",
    ],
    "what is your name": [
        "I'm RuleBot, your friendly rule-based assistant from DecodeLabs.",
    ],
    "who created you": [
        "I was built as Project 1 of the AI Engineering Internship at DecodeLabs.",
    ],
    "what can you do": [
        "Right now I can chat using simple predefined rules. "
        "Try asking me the time, or just say hello!",
    ],
    "time": [
        "TIME_INTENT",  # special marker handled dynamically below
    ],
    "help": [
        "You can say things like: hello, how are you, your name, what you can do, "
        "or time. Type 'bye' or 'exit' to leave.",
    ],
    "thank you": [
        "You're welcome!",
        "Anytime, happy to help!",
    ],
    "thanks": [
        "No problem at all!",
    ],
}

# Exit / kill commands that break the infinite loop
EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye", "see you"}

# Default fallback response when no rule matches
FALLBACK_RESPONSE = "I do not understand that yet. Type 'help' to see what I can do."


def sanitize_input(raw_text: str) -> str:
    """Phase 1: Input & Sanitization.
    Normalizes raw user input (case, whitespace, and trailing punctuation)
    so that 'Hello', ' hello ', 'HELLO', 'Hello!', and 'hello?' all match
    the same rule instead of falling through to the fallback response.
    """
    cleaned = raw_text.lower().strip()
    # Strip common trailing/leading punctuation (!, ?, ., ,) without
    # touching punctuation that might matter inside the sentence.
    cleaned = cleaned.strip(string.punctuation + " ")
    return cleaned


def get_response(user_input: str) -> str:
    """Process (Logic Skeleton): Intent Matching & Response Generation.
    Uses dictionary .get() for a single atomic lookup + fallback,
    instead of a long, unstable if-elif ladder.
    """
    # Nested condition example: smarter handling for a dynamic intent (time)
    responses = KNOWLEDGE_BASE.get(user_input)

    if responses is None:
        return FALLBACK_RESPONSE

    reply = random.choice(responses)

    # Handle dynamic responses (things that can't be hardcoded, like time)
    if reply == "TIME_INTENT":
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    return reply


def run_chatbot():
    """The Heartbeat: continuous input loop until the kill command."""
    print("=" * 55)
    print(" RuleBot - Rule-Based AI Chatbot (DecodeLabs Project 1)")
    print("=" * 55)
    print("Type 'help' to see what I can do, or 'bye' to exit.\n")

    while True:
        try:
            raw_input_text = input("You: ")
        except (EOFError, KeyboardInterrupt):
            # Fix: gracefully handle Ctrl+D / Ctrl+C instead of crashing
            # with an unhandled traceback.
            print("\nBot: Goodbye! Have a great day. 👋")
            break

        clean_input = sanitize_input(raw_input_text)

        # Kill command check
        if clean_input in EXIT_COMMANDS:
            print("Bot: Goodbye! Have a great day. 👋")
            break

        if clean_input == "":
            print("Bot: Please type something.")
            continue

        reply = get_response(clean_input)
        print(f"Bot: {reply}")


if __name__ == "__main__":
    run_chatbot()
