# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic word-guessing game while practicing Python strings, loops, conditionals, user input, and random selection. By the end of this assignment, you will have a complete game that tracks guesses and reports whether the player wins or loses.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Prepare the secret word and the variables needed to track the player's progress throughout the game.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list
- Initialize a collection to store the letters the player has guessed
- Set a maximum number of incorrect guesses and initialize the incorrect guess count

### 🛠️ Build the Game Loop

#### Description
Create the main game loop so the player can guess letters, reveal the hidden word, and reach a clear win or loss outcome.

#### Requirements
Completed program should:

- Accept one letter guess at a time from the player
- Display the current word progress using underscores for unguessed letters
- Record each guess and increase the incorrect guess count only when the letter is not in the secret word
- Show the letters already guessed and the number of incorrect guesses remaining
- End when the player guesses the word or uses all available attempts
- Display a clear win or loss message and reveal the secret word
