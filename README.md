Project 1: Rule-Based AI Chatbot


Goal

A simple rule-based chatbot that responds to predefined user inputs using
dictionary-based (if-else style) logic, running in a continuous loop.


How to Run

python3 chatbot.py

Features (matches the Project 1 spec)


• Input Loop: Continuous while True cycle (the "heartbeat").

• Sanitization: Input is lower-cased and stripped of whitespace.

• Knowledge Base: Dictionary with 9 intents (hello, hi, how are you, your name, who created you, what can you do, time, help, thank you/thanks).

• Fallback: A default response for anything not recognized.

• Exit Strategy: Clean "kill command" (bye, exit, quit, goodbye).

• Bonus (per Director's Tip / Conclusion slide):
Multiple varied responses per intent (feels less robotic).
A dynamic intent (time) showing the bot isn't purely static.
Clear docstrings explaining the "Input → Process → Output" architecture.


Sample Conversation

You: hello
Bot: Hi there! How can I help you today?
You: time
Bot: The current time is 07:46 AM.
You: bye
Bot: Goodbye! Have a great day. 👋


