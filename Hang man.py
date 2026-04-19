import tkinter as tk
import random

# Pastel Colours
BG = "#AFC9FF"
BTN = "#DCEBFF"
BTN_HOVER = "#CAE1FF"
BTN_TEXT = "#3A3A3A"
CORRECT = "#D4FFD6"
WRONG = "#FFD6E0"
TEXT = "#4A4A4A"
HEART = "❤️"

# Word List
WORD_PACKS = {
    "Animals": ["butterfly", "penguin", "rabbit", "dolphin", "kitten"],
    "Nature": ["rainbow", "ocean", "sunset", "forest", "breeze","earth","tree"],
    "Aesthetic": ["galaxy", "sparkle", "crystal", "harmony", "wonder"],
    "Adventure": ["treasure", "island", "fantasy", "journey", "mystery"]
}

ALL_WORDS = [word for pack in WORD_PACKS.values() for word in pack]

# Hint Generator (offline)
def generate_hint(word):
    for category, words in WORD_PACKS.items():
        if word in words:
            cat = category
            break
    else:
        cat = "General"

    return (
        f"✨ Starts with: {word[0].upper()}\n"
        f"✨ Ends with: {word[-1].upper()}\n"
        f"✨ Letters: {len(word)}\n"
        f"✨ Category: {cat}"
    )

# Start a New Game
def new_word():
    global chosen_word, display_word, attempts, hint_text
    chosen_word = random.choice(ALL_WORDS)
    display_word = ["_"] * len(chosen_word)
    attempts = 7
    hint_text = generate_hint(chosen_word)

    word_label.config(text=" ".join(display_word))
    attempts_label.config(text=HEART * attempts)
    hint_label.config(text="")
    message_label.config(text="")
    title_label.config(text=" Guess the Word!")

    for btn in letter_buttons:
        btn.config(state="normal", bg=BTN)

# Handle Guess
def guess(letter, btn):
    global attempts

    if letter in chosen_word:
        for i, ch in enumerate(chosen_word):
            if ch == letter:
                display_word[i] = letter

        btn.config(bg=CORRECT)
        word_label.config(text=" ".join(display_word))
        message_label.config(text="🌸 Nice! Keep going!", fg="#6AA84F")

        if "_" not in display_word:
            message_label.config(text="🎉 You won!", fg="#6AA84F")
            title_label.config(text="✨ Perfect! ✨")
            disable_buttons()
    else:
        attempts -= 1
        attempts_label.config(text=HEART * attempts)
        btn.config(bg=WRONG)
        message_label.config(text=" Try again!", fg="#D9534F")

        if attempts == 4:
            hint_label.config(text=hint_text)

        if attempts <= 0:
            word_label.config(text=chosen_word)
            message_label.config(text="❌ You lost!", fg="#D63E39")
            title_label.config(text="💔 Maybe next time!")
            disable_buttons()

    btn.config(state="disabled")

# Disable Buttons

def disable_buttons():
    for btn in letter_buttons:
        btn.config(state="disabled")

# Tkinter Window Setup

root = tk.Tk()
root.title("Pastel Hangman 🎀")
root.geometry("500x650")
root.config(bg=BG)

# Title
title_label = tk.Label(root, text="Pastel Hangman 🎀", font=("Helvetica", 28, "bold"), bg=BG, fg=TEXT)
title_label.pack(pady=10)

# Word display
word_label = tk.Label(root, text="", font=("Helvetica", 40, "bold"), bg=BG, fg=TEXT)
word_label.pack(pady=20)

# Attempts (Hearts)
attempts_label = tk.Label(root, text="", font=("Helvetica", 22), bg=BG, fg="#FF4B77")
attempts_label.pack(pady=5)

# Hint
hint_label = tk.Label(root, text="", font=("Helvetica", 14), bg=BG, fg=TEXT, justify="left")
hint_label.pack(pady=10)

# Message Display
message_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), bg=BG)
message_label.pack(pady=5)

# Alphabet Buttons Grid

letters_frame = tk.Frame(root, bg=BG)
letters_frame.pack()

letter_buttons = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
row = 0
col = 0

def on_enter(e):
    e.widget["bg"] = BTN_HOVER

def on_leave(e):
    e.widget["bg"] = BTN

for letter in alphabet:
    btn = tk.Button(
        letters_frame,
        text=letter,
        font=("Helvetica", 13, "bold"),
        width=4,
        height=1,
        bg=BTN,
        fg=BTN_TEXT,
        activebackground=BTN_HOVER,
        relief="raised",
        command=lambda l=letter.lower(), b=None: guess(l, button_map[l])
    )
    btn.grid(row=row, column=col, padx=4, pady=4)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    letter_buttons.append(btn)

    col += 1
    if col > 7:
        row += 1
        col = 0

button_map = {alphabet[i].lower(): letter_buttons[i] for i in range(26)}

# Restart button
restart_btn = tk.Button(
    root,
    text="New Word ",
    font=("Helvetica", 16, "bold"),
    bg="#FFF2B8",
    fg=TEXT,
    width=12,
    command=new_word
)
restart_btn.pack(pady=20)

# Start game
new_word()

root.mainloop()