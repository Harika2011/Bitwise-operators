import random
import os
import time

# --- Clear the screen ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Print the treasure map ---
def print_map(map_grid):
    for row in map_grid:
        print(" ".join(row))
    print()

# --- Directional hint function ---
def give_hint(row, col, treasure_row, treasure_col):
    hint = []
    if row > treasure_row:
        hint.append("⬆️ North")
    elif row < treasure_row:
        hint.append("⬇️ South")
    if col > treasure_col:
        hint.append("⬅️ West")
    elif col < treasure_col:
        hint.append("➡️ East")
    if not hint:
        return "🎯 You're right on it!"
    return "Hint: The treasure is " + " and ".join(hint) + "."

# --- Loading animation ---
def loading(message="Searching"):
    print(message, end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

# --- Main game function ---
def treasure_hunt():
    size = 5
    chances = 7
    map_grid = [["🟦" for _ in range(size)] for _ in range(size)]

    treasure_row = random.randint(0, size - 1)
    treasure_col = random.randint(0, size - 1)

    clear_screen()
    print("🏴‍☠️  WELCOME TO THE TREASURE HUNT! 🏝️\n")
    print("🌊 A mighty storm has stranded you on a mysterious island...")
    print("💎 Somewhere on this island lies a hidden treasure chest!")
    print(f"🧭 You have {chances} chances to find it. Choose wisely.\n")
    input("Press ENTER to begin your hunt... ")
    clear_screen()

    for attempt in range(1, chances + 1):
        print(f"🗺️  TREASURE MAP — Attempt {attempt} of {chances}\n")
        print_map(map_grid)

        # --- Player input ---
        try:
            row = int(input("Enter row (0–4): "))
            col = int(input("Enter column (0–4): "))
        except ValueError:
            print("⚠️ Invalid input! Enter numbers only between 0–4.")
            time.sleep(1.5)
            clear_screen()
            continue

        if not (0 <= row < size and 0 <= col < size):
            print("❌ Out of range! Please pick coordinates from 0–4.")
            time.sleep(1.5)
            clear_screen()
            continue

        if map_grid[row][col] == "❌":
            print("⚠️ You already searched here. Try another spot!")
            time.sleep(1.5)
            clear_screen()
            continue

        # --- Checking for treasure ---
        loading("Digging")
        if row == treasure_row and col == treasure_col:
            clear_screen()
            map_grid[row][col] = "💰"
            print("🎉 CONGRATULATIONS, EXPLORER! 🎉\n")
            print("🏆 You found the legendary treasure chest! 🏆\n")
            print_map(map_grid)
            print("🎊 Gold coins, jewels, and a pirate crown are now yours! 🪙💎👑")
            break
        else:
            map_grid[row][col] = "❌"
            print("💨 You dig through the sand... but find nothing.")
            print(give_hint(row, col, treasure_row, treasure_col))
            time.sleep(2)
            clear_screen()
    else:
        clear_screen()
        map_grid[treasure_row][treasure_col] = "💎"
        print("😢 Oh no! You ran out of chances!\n")
        print("The treasure remains buried in the sand forever...\n")
        print_map(map_grid)
        print(f"📍 It was hidden at row {treasure_row}, column {treasure_col}.")
        print("🏴‍☠️ Better luck on your next adventure, brave explorer!\n")

# --- Start the game ---
if __name__ == "__main__":
    treasure_hunt()
