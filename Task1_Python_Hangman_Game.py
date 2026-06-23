import random
# List of predefined words
words = ["Tendulkar", "Virat", "Gayle", "Yuvraj", "ABD"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

# Display hidden word
display_word = ["_"] * len(word)

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")

while attempts > 0 and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

# Result
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)
