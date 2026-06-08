
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game using Python strings, loops, and user input. You'll practice string manipulation, conditionals, random selection, and game logic.

## 📝 Tasks

### 🛠️ Set Up Word Selection and Display

#### Description
Create the foundation for the Hangman game by implementing word selection and a function to display the current game state with revealed and hidden letters.

#### Requirements
Completed program should:

- Define a predefined list of words to choose from
- Randomly select a word at the start of each game
- Create a function that displays the hidden word using underscores (e.g., `_ _ _ _`)
- Update the display when letters are guessed correctly
- Track and display incorrect guesses remaining (e.g., `Incorrect guesses remaining: 6`)


### 🛠️ Implement Game Logic and User Input

#### Description
Build the core game loop that handles letter guesses, validates input, updates game state, and determines win/lose conditions.

#### Requirements
Completed program should:

- Accept letter guesses from the user via `input()`
- Check if the guessed letter is in the word
- Update the hidden word display for correct guesses
- Track incorrect guesses and decrement remaining attempts
- End the game when the word is guessed completely or attempts run out
- Display appropriate win or lose messages with the final word revealed
