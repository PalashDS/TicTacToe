# Building a Tic-Tac-Toe Game Using Tkinter

import tkinter as tk  # Tkinter is used for the graphical user interface
from tkinter import messagebox  # This is used for showing dialog boxes

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")  # Set the window title

# Create a 3x3 grid of buttons to represent the Tic-Tac-Toe board
buttons = [[None for _ in range(3)] for _ in range(3)]

# Start with player "X"
player = "X"

def check_winner():
    """Check if any player has won the game."""
    
    # Check all rows and columns for the same symbol in a line
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True  # Winner found in a row
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True  # Winner found in a column

    # Check the diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True  # Winner found in the main diagonal
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True  # Winner found in the reverse diagonal

    return False  # No winner found

def disable_buttons():
    """Disable all buttons once the game ends."""
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")

def click(row, col):
    """Handle a button click event."""
    global player

    # Only allow a move if the clicked button is still empty
    if buttons[row][col]["text"] == "" and player != "":
        # Mark the button with the current player's symbol (X or O)
        buttons[row][col]["text"] = player

        # Check if the current player has won
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {player} wins!")
            disable_buttons()  # Disable all buttons after a win
        # Check if all buttons are filled and it's a tie
        elif all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            disable_buttons()  # Disable all buttons after a tie
        else:
            # Switch to the other player
            player = "O" if player == "X" else "X"

# Create the buttons and place them in the 3x3 grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('normal', 20), width=5, height=2,
                                  command=lambda i=i, j=j: click(i, j))
        buttons[i][j].grid(row=i, column=j)  # Arrange buttons in a grid layout

# Add a Reset button to restart the game
def reset_game():
    """Reset the game to its initial state."""
    global player
    player = "X"  # Reset to player X's turn
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")  # Clear all buttons

# Create and place the Reset button below the game grid
reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.grid(row=3, column=1)  # Place the Reset button in the middle

# Start the Tkinter main loop to keep the window running
root.mainloop()
