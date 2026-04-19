import random
import time

choices = ["Rock", "Paper", "Scissors"]
emoji = ["🪨", "📄", "✂️"]

# Welcome screen
print("\n" + "=" * 50)
print(" 🎮 WELCOME TO THE ROCK PAPER SCISSOR GAME 🎮")
print("=" * 50)
print("\n 👉Instructions:")
print("• Choose Rock, Paper or Scissors to play against the computer.")
print("• Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
print("• Type only the number shown in the menu.\n")
print("✨ Enjoy the game! ✨\n")

user_score = 0
computer_score = 0

while True:
    print("\n" + "-" * 50)
    print("📌 Make your choice:")
    print("1️⃣  Rock    🪨")
    print("2️⃣  Paper   📄")
    print("3️⃣  Scissors ✂️")
    print("0️⃣  Exit Game")
    print("-" * 50)

    user_input = input("👉 Enter your choice (1/2/3/0): ").strip()

    if user_input == "0":
        print("\n👋 Exiting game...")
        time.sleep(1)
        break

    if user_input not in ["1", "2", "3"]:
        print("\n❗ Oops! Invalid choice. Please enter 1, 2, 3, or 0.")
        continue

    user_index = int(user_input) - 1
    # Keep display as capitalized, but use lowercase for logic
    user_choice_display = choices[user_index]
    user_choice = choices[user_index].lower()
    user_emoji = emoji[user_index]

    computer_index = random.randint(0, 2)
    computer_choice_display = choices[computer_index]
    computer_choice = choices[computer_index].lower()
    computer_emoji = emoji[computer_index]

    print("\n🎯 You chose:", user_emoji, user_choice_display)
    print("🤖 Computer chose:", computer_emoji, computer_choice_display)

    # Game rules (all lowercase comparisons)
    if user_choice == computer_choice:
        print("😐 It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You win this round!")
        user_score += 1
    else:
        print("💥 Computer wins this round!")
        computer_score += 1

    print("\n📊  S C O R E B O A R D")
    print(f"✨ You: {user_score}   |   🤖 Computer: {computer_score}")

    time.sleep(1)

# Final display
print("\n" + "=" * 50)
print("🏁  G A M E   O V E R")
print("=" * 50)
print(f"✨ Final You: {user_score}")
print(f"🤖 Final Computer: {computer_score}")
print("🎉 Thanks for playing! See you again!")
print("=" * 50 + "\n")
