import time
import random

# List of sentences to choose from
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Practice makes perfect when learning to type.",
    "Artificial intelligence is transforming the world.",
    "Never stop learning and exploring new things."
]

# Select a random sentence
sentence = random.choice(sentences)
print("Type the following sentence:")
print(sentence)

# Start the timer
start_time = time.time()

# Get user input
user_input = input("\nStart typing: ")

# Stop the timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

# Count words in user input
word_count = len(user_input.split())

# Calculate WPM
wpm = word_count / (elapsed_time / 60)

# Count correct characters
correct_chars = sum(1 for a, b in zip(user_input, sentence) if a == b)
total_chars = len(sentence)

# Calculate accuracy percentage
accuracy = (correct_chars / total_chars) * 100

# Display results
print("\nTest Completed!")
print(f"Time Taken: {elapsed_time:.2f} seconds.")
print(f"Typing Speed: {wpm:.2f} WPM")
print(f"Accuracy: {accuracy:.2f}%")
