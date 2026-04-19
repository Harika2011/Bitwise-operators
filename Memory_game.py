import tkinter as tk
import random

#Memory Match Game

# Task:Flip any two cards to find a matching pair
# Matching cards stay revealed until all pairs r found

# The main window
root = tk.Tk()
root.title("🧠 Memory match game")

#List of emojis for 8 pairs
symbols=['🍎', '🍌', '🍇', '🍒', '🍉', '🍍', '🥝', '🍋']

#Duplicate each emoji to make pairs,then shuffle
cards = symbols*2
random.shuffle(cards)

#arranging the cards into a 4x4 grid
grid=[cards[i*4:(i+1)*4]for i in range(4)]

#tracking the matched cards using boolean 
revealed = [[False]*4 for _ in range(4)]

#Refrence to all buttons 
buttons=[[None]*4 for _ in range(4)]

#storing the value of the first selected card
first_choice = None

#score of the number of pairs found
pairs_found = 0

# FUNCTION: Handle card click

def on_click(r, c):
    """Handles what happens when a player clicks a card."""
    global first_choice, pairs_found

    # If the card is already revealed, ignore the click
    if revealed[r][c]:
        return

    # Show the emoji and disable the button temporarily
    buttons[r][c].config(text=grid[r][c], state="disabled")

    # If it's the first card flipped
    if not first_choice:
        first_choice = (r, c)
    else:
        # Second card flipped
        r1, c1 = first_choice

        # Check if both cards match
        if grid[r][c] == grid[r1][c1]:
            revealed[r][c] = revealed[r1][c1] = True
            pairs_found += 1

            # Check for win
            if pairs_found == 8:
                win_label.config(text="🎉 You found all pairs! Great job! 🎉")
        else:
            # Not a match → hide both cards after short delay
            root.after(800, lambda: hide_cards(r, c, r1, c1))

        # Reset for next turn
        first_choice = None


# FUNCTION: Hide unmatched cards

def hide_cards(r, c, r1, c1):
    """Turns unmatched cards face down again."""
    buttons[r][c].config(text="❓", state="normal")
    buttons[r1][c1].config(text="❓", state="normal")


# CREATE THE 4x4 BUTTON GRID

for i in range(4):
    for j in range(4):
        # Use a lambda to pass the row & column to on_click()
        btn = tk.Button(
            root,
            text="❓",               # Hidden card
            width=6,
            height=3,
            font=("Arial", 16, "bold"),
            bg="#203354",           # Dark blue background
            fg="white",
            relief="raised",
            command=lambda r=i, c=j: on_click(r, c)
        )
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = btn


# WIN MESSAGE LABEL

win_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    fg="green"
)
win_label.grid(row=5, column=0, columnspan=4, pady=10)

# RUN THE GAME

root.mainloop()