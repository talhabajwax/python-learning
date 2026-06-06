import random
random_words = ["python", "programming", "hangman", "challenge", "developer"]
word = random.choice(random_words)
hidden_word = ["_"] * len(word)
print("Welcome to Hangman!")
print("Guess the word:")
for i in hidden_word:
    print(i, end=" ")
lives = 6

