# MUSICAL CHAIRS
# Using bubble sort 
# score 
# name of players 
# elminate players 

import random
import time

def bubble_sort(players):
    n = len(players)
    for i in range(n):
        for j in range(0, n - i - 1):
            if players[j]["score"] > players[j + 1]["score"]:
                players[j], players[j + 1] = players[j + 1], players[j]

auto_names = [
    "Alex", "Jordan", "Sam", "Chris", "Taylor",
    "Morgan", "Jamie", "Riley", "Casey", "Avery"
]

MIN_PLAYERS = 5

user_players = int(input("Enter number of players: "))
players = []

total_players = max(user_players, MIN_PLAYERS)

for i in range(user_players):
    name = input(f"Enter name of player {i + 1}: ")
    players.append({"name": name, "score": 0})

extra_needed = total_players - user_players
random.shuffle(auto_names)

for i in range(extra_needed):
    players.append({"name": auto_names[i], "score": 0})

print("\n🎶 Musical Chairs Game Started 🎶")
print(f"Players participating: {len(players)}\n")

round_num = 1

# Game loop
while len(players) > 1:
    print(f"--- Round {round_num} ---")
    print("Music is playing...")
    time.sleep(1.5)
    print("Music stopped! 🪑\n")

    for p in players:
        p["score"] = random.randint(1, 100)

    print("Scores:")
    for p in players:
        print(f"{p['name']}: {p['score']}")

    bubble_sort(players)

    eliminated = players.pop(0)
    print(f"\n❌ {eliminated['name']} is eliminated!\n")

    round_num += 1
    time.sleep(1.5)

print("🏆 WINNER 🏆")
print(f"{players[0]['name']} wins Musical Chairs! 🎉")