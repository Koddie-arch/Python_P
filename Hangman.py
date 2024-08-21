import random

# Define the hangman stages
HANGMAN_STAGES = [
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
 ''',
    r'''
   +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
 ''',
    r'''
   +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
 ''',
    r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    r'''
 +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
    r'''
 +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
    r'''
 +---+
  |   |
      |
      |
      |
      |
=========
'''
]

# Define the word chart
WORD_CHART = ["ardvark", "baboon", "camel"]

def play_hangman():
    # Choose a random word from the word chart
    chosen_word = random.choice(WORD_CHART)

    # Initialize the lives and display
    lives = 6
    display = ["_"] * len(chosen_word)

    # Game loop
    while True:
        # Ask the user for a guess
        guess = input("Guess a letter? ").lower()

        # Check if the guess is in the chosen word
        for position, letter in enumerate(chosen_word):
            if letter == guess:
                display[position] = letter

        # If the guess is not in the chosen word, decrement the lives
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                print("You lose!")
                break

        # Print the current state of the game
        print(" ".join(display))
        print(HANGMAN_STAGES[lives])

        # Check if the user has won
        if "_" not in display:
            print("You win!")
            break

if __name__ == "__main__":
    play_hangman()