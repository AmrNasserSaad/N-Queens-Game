import tkinter as tk
from tkinter import messagebox

class NQueensGame:
    def __init__(self, master, board_size):
        self.master = master
        self.board_size = board_size
        self.board = [[0] * board_size for _ in range(board_size)]
        self.create_board()

    def create_board(self):
        self.buttons = [[None] * self.board_size for _ in range(self.board_size)]
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.buttons[i][j] = tk.Button(self.master, width=5, height=2, bg="white" if (i + j) % 2 == 0 else "black", font=('Helvetica', 14),
                        command=lambda row=i, col=j: self.toggle_queen(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def toggle_queen(self, row, col):
        if self.board[row][col] == 1:
            self.remove_queen(row, col)
        else:
            self.add_queen(row, col)

    def add_queen(self, row, col):
        if self.is_safe(row, col):
            self.board[row][col] = 1
            self.update_board()
        else:
            messagebox.showerror(title="Invalid move!", message=f'Queens can attack each other by this move!')

    def remove_queen(self, row, col):
        self.board[row][col] = 0
        self.update_board()

    def is_safe(self, row, col):
        for i in range(self.board_size):
            if self.board[i][col] == 1 or self.board[row][i] == 1:
                return False
        
        for j in range(self.board_size):
            upper_left_diagonal_row = col - (row - j)
            upper_right_diagonal_row = col + (row - j)
        
            if (0 <= upper_left_diagonal_row < self.board_size and self.board[j][upper_left_diagonal_row] == 1):
                return False
        
            if (0 <= upper_right_diagonal_row < self.board_size and self.board[j][upper_right_diagonal_row] == 1):
                return False
            
        return True

    def update_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == 1:
                    self.buttons[i][j].config(text="Q", state=tk.NORMAL, foreground="black" if (i + j) % 2 == 0 else "white")
                else:
                    self.buttons[i][j].config(text="", state=tk.NORMAL)

        self.active_queens = sum(row.count(1) for row in self.board)
        if self.active_queens == self.board_size:
            messagebox.showinfo(title="You Won!", message=f'This game is made by:\nAmr Fouad Fahmy \nAmr Nasser Saad\nOmar Mohamed El-Sayed\nFares Ahmed Ali\nFares Mansouf\nSection 5')

def start_game():
    try:
        board_size = int(entry.get())
        if 4 <= board_size <= 15:
            window.destroy()
            root = tk.Tk()
            root.title("N-Queens Game")
            # Set window size to match game window
            root.geometry("500x500")
            game = NQueensGame(root, board_size)
            root.mainloop()
        else:
            messagebox.showerror(title="Error", message="Please choose a number between 4 and 15.")
    except ValueError:
        messagebox.showerror(title="Error", message="Please enter a valid number.")

# Create main window
window = tk.Tk()
window.title("N-Queens Game")
# Set window size to have more negative space
window.geometry("500x500")

# Label and Entry for board size input
label = tk.Label(window, text="Enter Board size:", font=('Helvetica', 16))
label.pack(pady=20)
entry = tk.Entry(window, font=('Helvetica', 14))
entry.pack(pady=10)

# Button to start the game
start_button = tk.Button(window, text="Start Game", font=('Helvetica', 14), command=start_game)
start_button.pack(pady=20)

window.mainloop()
