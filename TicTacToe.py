import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.root = root
        self.root.title("T^4 - A Twisty Tic Tac Toe")
        self.board_size = 3
        self.current_player = "X"
        self.root.geometry("415x420")
        self.board = [""] * (self.board_size ** 2)
        
        self.label = tk.Label(root, text="Tic Tac Toe", font=("Helvetica", 16, "bold"))
        self.label.grid(row=0, column=0, columnspan=self.board_size)
        
        self.buttons = []
        self.key_bindings = {}  
        key_sequence = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                btn = tk.Button(root, text="", font=("Helvetica", 24), width=7, height=3,
                                command=lambda i=i, j=j: self.on_button_click(i, j), bg="yellow")
                btn.grid(row=i + 1, column=j) 
                row.append(btn)
                
              
                key = key_sequence[i * self.board_size + j]
                self.key_bindings[key] = (i, j)
                self.root.bind(key, self.on_key_press)
                
            self.buttons.append(row)

    def on_key_press(self, event):
        key = event.keysym
        if key in self.key_bindings:
            i, j = self.key_bindings[key]
            self.on_button_click(i, j)

    def remove_random_tokens(self):
        available_positions = [i for i, token in enumerate(self.board) if token != ""]
        random_positions = random.sample(available_positions, 3)
        for position in random_positions:
            self.board[position] = ""
        self.update_buttons()

    def on_button_click(self, row, col):
        if self.board[row * self.board_size + col] == "":
            self.board[row * self.board_size + col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                self.remove_random_tokens() 
                self.update_buttons()
                self.current_player = "O" if self.current_player == "X" else "X"
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def update_buttons(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.buttons[i][j].config(text=self.board[i * self.board_size + j])

    def check_winner(self):
        for i in range(self.board_size):
            if all(self.board[i * self.board_size + j] == self.current_player for j in range(self.board_size)):
                return True
            if all(self.board[j * self.board_size + i] == self.current_player for j in range(self.board_size)):
                return True
        if all(self.board[i * (self.board_size + 1)] == self.current_player for i in range(self.board_size)):
            return True
        if all(self.board[(i + 1) * (self.board_size - 1)] == self.current_player for i in range(self.board_size)):
            return True
        return False

    def reset_board(self):
        self.current_player = "X"
        self.board = [""] * (self.board_size ** 2)
        self.update_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
