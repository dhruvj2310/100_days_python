import random

# List of words
word_list = [
    "python", "apple", "computer", "keyboard",
    "monitor", "program", "science", "hangman",
    "internet", "developer"
]

# Hangman stages
gallow_steps = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]

# ------------------- START -------------------

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ["_"] * word_length

lives = 6
game_over = False

print("WELCOME TO HANGMAN!\n")

while not game_over:

    print(gallow_steps[6 - lives])
    print("Word:", " ".join(display))

    guess = input("\nGuess a letter: ").lower()

    # Already guessed
    if guess in display:
        print(f"You already guessed '{guess}'.")

    # Check every letter
    found = False

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
            found = True

    # Wrong guess
    if not found:
        lives -= 1
        print(f"'{guess}' is not in the word.")
        print(f"Lives left: {lives}")

    # Win condition
    if "_" not in display:
        print("\nCongratulations! You guessed the word!")
        print("Word:", chosen_word)
        game_over = True

    # Lose condition
    if lives == 0:
        print(gallow_steps[6])
        print("\nGAME OVER!")
        print("The word was:", chosen_word)
        game_over = True