def display_towers(towers):
    print("\n🗼 Towers State:")
    max_height = max(len(t) for t in towers)
    for level in range(max_height - 1, -1, -1):
        for tower in towers:
            if level < len(tower):
                print(f"  {tower[level]}  ", end=' ')
            else:
                print("  |  ", end=' ')
        print()
    print(" ----  ----  ----")
    print("  0     1     2\n")

def is_valid_move(towers, from_rod, to_rod):
    if not towers[from_rod]:
        print("⚠️ No disks to move on that rod.")
        return False
    if towers[to_rod] and towers[to_rod][-1] < towers[from_rod][-1]:
        print("⛔ Invalid move! Cannot place larger disk on smaller one.")
        return False
    return True

def main():
    print("🎮 Welcome to the Tower of Hanoi!")
    while True:
        try:
            num_disks = int(input("Enter the number of disks (1 or more): "))
            if num_disks < 1:
                raise ValueError
            break
        except ValueError:
            print("❌ Please enter a valid positive number.")

    towers = [list(range(num_disks, 0, -1)), [], []]
    display_towers(towers)

    while True:
        move = input("👉 Enter your move (from_rod to_rod) or type 'quit': ").strip().lower()
        if move == 'quit':
            print("👋 Thanks for playing!")
            break
        try:
            from_rod, to_rod = map(int, move.split())
            if from_rod not in (0, 1, 2) or to_rod not in (0, 1, 2):
                raise ValueError
            if is_valid_move(towers, from_rod, to_rod):
                towers[to_rod].append(towers[from_rod].pop())
                display_towers(towers)
                if towers[2] == list(range(num_disks, 0, -1)):
                    print("🎉 Congratulations! You've solved the puzzle.")
                    break
        except ValueError:
            print("❌ Invalid input. Example move: '0 2' (from rod 0 to rod 2)")

if __name__ == '__main__':
    main()
