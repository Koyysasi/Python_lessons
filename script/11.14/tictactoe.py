import tkinter as tk
from tkinter import messagebox
import sqlite3

class TicTacToe:
    def __init__(self, root, size=3):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.size = size
        self.player = "X"
        self.board = [""] * (size * size)
        self.buttons = []

        self.create_buttons()
        self.setup_database()

    def create_buttons(self):
        for i in range(self.size * self.size):
            button = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//self.size, column=i%self.size, padx=5, pady=5)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.player} wins!")
                self.save_result(self.player)
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.save_result("Tie")
                self.reset_game()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        # Check rows
        for row in range(self.size):
            if all(self.board[row*self.size + col] == self.player for col in range(self.size)):
                return True

        # Check columns
        for col in range(self.size):
            if all(self.board[row*self.size + col] == self.player for row in range(self.size)):
                return True

        # Check diagonals
        if all(self.board[i*self.size + i] == self.player for i in range(self.size)):
            return True
        if all(self.board[i*self.size + (self.size - 1 - i)] == self.player for i in range(self.size)):
            return True

        return False

    def reset_game(self):
        self.board = [""] * (self.size * self.size)
        for button in self.buttons:
            button.config(text="")
        self.player = "X"

    def setup_database(self):
        self.conn = sqlite3.connect('tictactoe.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                winner TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def save_result(self, winner):
        self.cursor.execute('INSERT INTO results (winner) VALUES (?)', (winner,))
        self.conn.commit()

    def __del__(self):
        self.print_results()
        self.conn.close()

    def print_results(self):
        self.cursor.execute('SELECT winner, COUNT(*) FROM results GROUP BY winner')
        results = self.cursor.fetchall()
        print("Game Results:")
        for winner, count in results:
            print(f"{winner}: {count} wins")

if __name__ == "__main__":
    root = tk.Tk()
    size = int(input("Enter the size of the Tic Tac Toe board: "))
    game = TicTacToe(root, size)
    root.mainloop()