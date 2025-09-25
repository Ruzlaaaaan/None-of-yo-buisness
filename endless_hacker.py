import random
import time
import string

# ANSI escape codes for colors
colors = [
    '\033[91m',  # Red
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[96m',  # Cyan
    '\033[97m',  # White
    '\033[90m',  # Black
    '\033[31m',  # Bright Red
    '\033[32m',  # Bright Green
    '\033[33m',  # Bright Yellow
    '\033[34m',  # Bright Blue
    '\033[35m',  # Bright Magenta
    '\033[36m',  # Bright Cyan
    '\033[37m'   # Bright White
]

reset = '\033[0m'  # Reset to default color

# Hacker-like phrases
phrases = [
    "Accessing mainframe...",
    "Decrypting data...",
    "Bypassing firewall...",
    "Injecting payload...",
    "Scanning ports...",
    "Cracking password...",
    "Uploading virus...",
    "Downloading files...",
    "Establishing connection...",
    "Hacking in progress..."
]

while True:
    # Randomly choose to print a phrase or random string
    if random.choice([True, False]):
        # Print a hacker phrase
        color = random.choice(colors)
        phrase = random.choice(phrases)
        print(color + phrase + reset)
    else:
        # Print random string
        color = random.choice(colors)
        length = random.randint(20, 80)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        print(color + random_string + reset)
    
    time.sleep(0.001)  # Very fast delay of 1 millisecond
