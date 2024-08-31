# 🎮 Master Mind Game

## Overview

This Python project is an implementation of the classic "Master Mind" game, where the player (code breaker) tries to guess the secret code set by the program (code maker). The player has 15 attempts to guess the correct sequence of colors, and the program provides feedback after each guess in the form of black and white scores.

- **Black score**: Correct color in the correct position.
- **White score**: Correct color in the wrong position.

The game ends either when the player successfully guesses the correct sequence or exhausts the allowed number of guesses or penalties.

## Features

- **Interactive gameplay**: Users can input their guesses, and the program provides real-time feedback.
- **Error handling**: The game checks for repeated colors, invalid inputs, and insufficient guesses, assigning penalties where necessary.
- **Random code generation**: The code maker selects a random sequence of 4 colors from a list of 10 available colors.

## How to Play

1. Run the game.
2. The program will display the available colors.
3. Enter your name to start.
4. Input your guesses based on the colors provided.
5. The program will provide feedback after each guess.
6. Win by guessing the correct sequence within 15 attempts and avoiding 5 penalties!

## Example

```
What is your name? Hannah
Welcome to Master Mind Hannah!
The code maker is here. Available colors are:
Red, Yellow, Blue, Green, Orange, Pink, Purple, Cyan, Silver, Teal

You can start guessing Hannah.
Enter guess number 1: Red Pink Cyan Yellow
You got 0 black, and 1 white for this guess.
...
Enter guess number 7: Orange red blue silver
You got 4 blacks Hannah.
You won the game with 7 guesses and 4 penalties, Congratulations.
```
Thank you for viewing!
