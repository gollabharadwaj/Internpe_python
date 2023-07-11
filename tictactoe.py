import random
import tkinter as tk
from tkinter import messagebox

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# Function to handle button clicks
def handleButtonClick(row, col):
    global currentPlayer, gameRunning
    if board[row*3 + col] == "-":
        board[row*3 + col] = currentPlayer
        button_grid[row][col].configure(text=currentPlayer)
        checkIfWin()
        checkIfTie()
        switchPlayer()
        if currentPlayer == "O" and gameRunning:
            computerMove()

# Function to check for a win
def checkIfWin():
    global winner, gameRunning
    # Check horizontal lines
    for row in range(3):
        if board[row*3] == board[row*3 + 1] == board[row*3 + 2] != "-":
            winner = board[row*3]
            gameRunning = False
            messagebox.showinfo("Game Over", f"The winner is {winner}!")
            resetBoard()
            return
    # Check vertical lines
    for col in range(3):
        if board[col] == board[col + 3] == board[col + 6] != "-":
            winner = board[col]
            gameRunning = False
            messagebox.showinfo("Game Over", f"The winner is {winner}!")
            resetBoard()
            return
    # Check diagonal lines
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        gameRunning = False
        messagebox.showinfo("Game Over", f"The winner is {winner}!")
        resetBoard()
        return
    if board[2] == board[4] == board[6] != "-":
        winner = board[2]
        gameRunning = False
        messagebox.showinfo("Game Over", f"The winner is {winner}!")
        resetBoard()
        return

# Function to check for a tie
def checkIfTie():
    global gameRunning
    if "-" not in board:
        gameRunning = False
        messagebox.showinfo("Game Over", "It's a tie!")
        resetBoard()

# Function to switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Function for computer move
def computerMove():
    global currentPlayer
    while currentPlayer == "O" and gameRunning:
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = currentPlayer
            button_grid[position//3][position%3].configure(text=currentPlayer)
            checkIfWin()
            checkIfTie()
            switchPlayer()

# Function to reset the game board
def resetBoard():
    global board, currentPlayer, gameRunning
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    currentPlayer = "X"
    gameRunning = True
    for row in range(3):
        for col in range(3):
            button_grid[row][col].configure(text="-")

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create a grid of buttons for the game board
button_grid = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text="-", width=10, height=4,
                           command=lambda r=row, c=col: handleButtonClick(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    button_grid.append(button_row)

# Run the main event loop
root.mainloop()
