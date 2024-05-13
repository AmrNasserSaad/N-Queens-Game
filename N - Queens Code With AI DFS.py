import tkinter as tk
from tkinter import messagebox

class InitialWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Enter Board Size")
        self.root.geometry("500x500")  # Larger window size
        
        self.label = tk.Label(self.root, text="Enter Board size:", font=("Helvetica", 16))  # Bigger text
        self.label.pack(pady=20)  # Add space around the text
        
        self.entry = tk.Entry(self.root, font=("Helvetica", 14))  # Bigger entry font
        self.entry.pack(pady=10)  # Add space around the entry
        
        self.button = tk.Button(self.root, text="Start Game", command=self.start_game, font=("Helvetica", 14))  # Bigger button font
        self.button.pack()  # Add space around the button

        
    def start_game(self):
        board_size = self.entry.get()
        if board_size.isdigit() and 4 <= int(board_size) <= 15:
            self.root.destroy()
            NQueensGame(int(board_size))
        else:
            messagebox.showerror(title="Error", message="Please choose a number between 4 and 15.")


class NQueensGame:
    def __init__(self, board_size):
        # Preparing the environment
        self.board_size = board_size
        self.root = tk.Tk() # Creates the main window
        self.root.title("N-Queens Game") # Title of the window
        self.buttons = [[None] * board_size for _ in range(board_size)]
        # Create the chessboard
        self.create_board()
        # Begin solving the game
        self.solve()

    def solve(self):
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self._solve_dfs(0)

    def _solve_dfs(self, col):
        # Prevents the function from calling itself again when col == board size
        if col == self.board_size:
            return True

        for row in range(self.board_size):
            if self.is_safe(row, col):
                # If the selected cell is safe, mark it and move to the next column
                self.board[row][col] = 1
                self.update_board(row, col, True)
                if self._solve_dfs(col + 1):
                    return True
                # If the placement doesn't lead to a solution, backtrack
                self.board[row][col] = 0
                self.update_board(row, col, False)

        return False

    def is_safe(self, row, col):
        # Check column
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.board_size), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def create_board(self):
        # 2 for loops to iterate through rows and columns
        for i in range(self.board_size):
            for j in range(self.board_size):
                button = tk.Button(self.root, width=5, height=2)
                button.grid(row=i, column=j)
                if (i + j) % 2 == 0:
                    button.config(bg="white", width=5, height=2,font=('Helvetica', 14))
                else:
                    button.config(bg="black", fg="white", width=5, height=2,font=('Helvetica', 14))
                self.buttons[i][j] = button

    def update_board(self, row, col, place):
        # Function to place or remove queen dynamically with a delay
        if place:
            self.root.after(col * 1000, lambda row=row, col=col: self.buttons[row][col].config(text="Q", font=('Helvetica', 14), width=5, height=2))
        else:
            self.root.after(col * 1000, lambda row=row, col=col: self.buttons[row][col].config(text="", width=5, height=2))
        self.root.update()

# Display the initial window to get the board size from the user
InitialWindow()
tk.mainloop()
