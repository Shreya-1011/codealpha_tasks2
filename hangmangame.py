import random

# List of words to choose from
word_list = ['python', 'hangman', 'computer', 'programming', 'chatbot']

# Choose a random word
word = random.choice(word_list)

# Store guessed letters
guessed_letters = []

tries = 6

display = ['_'] * len(word)

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Main game loop
while tries > 0 and '_' in display:
    print("\nWord:", ' '.join(display))
    print("Tries left:", tries)
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        tries -= 1

if '_' not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over! The word was:", word)
