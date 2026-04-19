import tkinter as tk
from tkinter import messagebox

Cell_Size = 50
Grid_Rows = 5
Grid_Cols = 5

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🐭 MazePath - Escape the Maze!")

        self.grid = [[1 for _ in range(Grid_Cols)] for _ in range(Grid_Rows)]

        self.canvas = tk.Canvas(root, width=Grid_Cols*Cell_Size, height=Grid_Rows*Cell_Size, bg="white")
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.toggle_cell)

        self.button = tk.Button(root, text="🔍 Find Paths", command=self.find_paths, font=("Arial", 12))
        self.button.pack(pady=5)

        self.result = tk.Label(root, text="", font=("Arial", 14), fg="blue")
        self.result.pack()

        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        for row in range(Grid_Rows):
            for col in range(Grid_Cols):
                color = "white" if self.grid[row][col] == 1 else "black"
                x0 = col * Cell_Size
                y0 = row * Cell_Size
                x1 = x0 + Cell_Size
                y1 = y0 + Cell_Size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="gray")

    def toggle_cell(self, event):
        col = event.x // Cell_Size
        row = event.y // Cell_Size
        if 0 <= row < Grid_Rows and 0 <= col < Grid_Cols:
            self.grid[row][col] = 1 - self.grid[row][col]
            self.draw_grid()

    def find_paths(self):
        if self.grid[0][0] == 0 or self.grid[Grid_Rows - 1][Grid_Cols - 1] == 0:
            self.result.config(text="Start or End blocked!", fg="red")
            return

        dp = [[-1 for _ in range(Grid_Cols)] for _ in range(Grid_Rows)]

        def is_valid(x, y):
            return 0 <= x < Grid_Rows and 0 <= y < Grid_Cols and self.grid[x][y] == 1

        def count_paths(x, y):
            if not is_valid(x, y):
                return 0
            if x == Grid_Rows - 1 and y == Grid_Cols - 1:
                return 1
            if dp[x][y] != -1:
                return dp[x][y]
            dp[x][y] = count_paths(x + 1, y) + count_paths(x, y + 1)
            return dp[x][y]

        total_paths = count_paths(0, 0)
        self.result.config(text=f"✅ Total Paths: {total_paths}", fg="green" if total_paths else "red")


if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()
