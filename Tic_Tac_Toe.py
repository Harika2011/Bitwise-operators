import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the board
def display_board(board):
    clear_screen()
    print("✨ TIC TAC TOE ✨")
    print()
    print("     1 | 2 | 3")
    print("    ---+---+---")
    print("     4 | 5 | 6")
    print("    ---+---+---")
    print("     7 | 8 | 9")
    print()
    print("Current Board:")
    print()
    print(f"     {board[0]} | {board[1]} | {board[2]}")
    print("    ---+---+---")
    print(f"     {board[3]} | {board[4]} | {board[5]}")
    print("    ---+---+---")
    print(f"     {board[6]} | {board[7]} | {board[8]}")
    print()

# Check win
def check_win(board, p):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(board[a] == board[b] == board[c] == p for a,b,c in wins)

# Check draw
def check_draw(board):
    return all(space != " " for space in board)

# Main game function
def play_game():
    board = [" "] * 9
    player = "X"

    while True:
        display_board(board)
        print(f"Player {player}'s turn!")
        
        try:
            move = int(input("➡️  Enter a position (1-9): "))
            
            if not (1 <= move <= 9):
                print("❌ Choose between 1 and 9!")
                time.sleep(1)
                continue

            if board[move - 1] != " ":
                print("❌ That spot is already taken!")
                time.sleep(1)
                continue
        except:
            print("❌ Enter a valid number!")
            time.sleep(1)
            continue

        board[move - 1] = player

        # Check win
        if check_win(board, player):
            display_board(board)
            print(f"🎉 CONGRATULATIONS! Player {player} wins!")
            break

        # Check draw
        if check_draw(board):
            display_board(board)
            print("🤝 It's a DRAW!")
            break

        # Switch players
        player = "O" if player == "X" else "X"

    print()
    input("Press ENTER to continue...")

# Loop for replay
while True:
    clear_screen()
    print("🎮 Welcome to Interactive Tic Tac Toe!")
    print("Players: X & O")
    print("To play, enter the number from 1–9 based on the grid.")
    print()
    
    play_game()
    
    choice = input("Play again? (y/n): ").lower()
    if choice != "y":
        print("👋 Thanks for playing!")
        break
