
# 📘 Assignment: Hangman

## 🎯 Objective

Build a command-line Hangman game in Python that practices string manipulation, control flow, and user input.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Implement a playable Hangman game that selects a random word, accepts single-letter guesses, displays progress, and ends with a clear win or lose result.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (starter-code provided)
- Accept single-letter guesses (case-insensitive) and reveal correctly guessed letters in the displayed word
- Show current progress as underscores and revealed letters (e.g., `_ a _ g _ a _`)
- Track and display remaining attempts; decrement on incorrect guesses
- Remember and display previously guessed letters and avoid repeated penalties for the same guess
- End the game with a win message when the word is fully revealed or a lose message that reveals the correct word
- Include simple input validation and friendly prompts

#### Example

```
Word: _ _ _ _ _
Guess a letter: a
Correct! Word: a _ _ _ _
Guesses left: 6
```

#### Files

- Starter code: `assignments/games-in-python/starter-code.py`

Follow the structure and headings in `templates/assignment-template.md` when adding or updating assignment content.
