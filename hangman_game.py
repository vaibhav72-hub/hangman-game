import random

# List of words to choose from
words = ['python', 'programming', 'hangman', 'challenge', 'tutorial']

def select_word():
    return random.choice(words)

def display_word(word, guesses):
    return ' '.join([letter if letter in guesses else '_' for letter in word])

def hangman():
    word = select_word()
    guesses = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # You can set this limit

    print("Welcome to Hangman!")
    print(display_word(word, guesses))
    print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}\n")

    while incorrect_guesses < max_incorrect_guesses and set(word) != guesses:
        guess = input("Guess a letter: ").lower()
        if guess in guesses:
            print(f"You've already guessed '{guess}'. Try again.")
        elif guess in word:
            guesses.add(guess)
            print("Correct!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! The letter '{guess}' is not in the word.")
        
        print(display_word(word, guesses))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}\n")

    if set(word) == guesses:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"Game over! The correct word was: {word}")

if __name__ == "__main__":
    hangman()
