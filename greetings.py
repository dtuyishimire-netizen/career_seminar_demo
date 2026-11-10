# A super simple international greeting app for Git demo!

import random

# List of greetings
greetings = [
    "Muraho! (Kinyarwanda)",
    "Hello! (English)",
    "Jambo! (Swahili)",
]

print("\n✨ *** GREETING WALL *** ✨\n")

# Pick and display one random greeting from the list
welcome_message = random.choice(greetings)
print("Welcome Message:", welcome_message)

print("\nTotal languages represented:", len(greetings))
