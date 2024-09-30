# 🕹️ Tic-Tac-Toe Game with Tkinter

## Overview
This is a simple **Tic-Tac-Toe** game implemented in Python using the Tkinter library for the GUI. The game is designed for two players who take turns marking a 3x3 grid with either `X` or `O`. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

### Features:
- 🏆 Detects when a player wins or when the game ends in a draw.
- 🔄 Allows resetting the game board to start a new round.
- 👤 Two-player mode with alternating turns.

## How to Run the Project

### Prerequisites
- **Python 3.x** installed on your machine.
- Tkinter library (this usually comes with standard Python installations).

### Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/PalashDS/TicTacToe.git

### Key Functions
- **check_winner():**
Checks rows, columns, and diagonals to see if there is a winner.

- **disable_buttons():**
Disables all buttons once the game has ended.

- **click(row, col):**
Called when a player clicks on a square. It updates the square with the current player's mark and checks for a win or tie.

- **reset_game():**
Clears the board and resets the game for a new round.