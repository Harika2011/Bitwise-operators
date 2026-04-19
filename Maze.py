import tkinter as tk
import random
import math

TILE = 24
ROWS = COLS = 21
SPEED = 130
CHASE_RANGE = 6

WALL = "#0ab1ff"
COIN = "#ffd84d"
PLAYER_COLOR = "yellow"
GHOST_COLOR = "red"
VULNERABLE = "#66ccff"

# -------------------------------------------
# MAZE GENERATION (DFS BACKTRACKING)
# -------------------------------------------
def generate_maze(n):
    maze = [["#" for _ in range(n)] for _ in range(n)]

    def carve(r, c):
        dirs = [(2,0),(-2,0),(0,2),(0,-2)]
        random.shuffle(dirs)

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 1 <= nr < n-1 and 1 <= nc < n-1 and maze[nr][nc] == "#":
                maze[r+dr//2][c+dc//2] = " "
                maze[nr][nc] = " "
                carve(nr, nc)

    maze[1][1] = " "
    carve(1,1)

    # Fill corridors with coins
    for r in range(n):
        for c in range(n):
            if maze[r][c] == " ":
                maze[r][c] = "."

    # Power pellets in 4 corners
    maze[1][1] = "o"
    maze[1][n-2] = "o"
    maze[n-2][1] = "o"
    maze[n-2][n-2] = "o"

    return maze

grid = generate_maze(ROWS)

# -------------------------------------------
# GLOBALS
# -------------------------------------------
px, py = 1, 1
gx, gy = ROWS-2, COLS-2
dir_x = dir_y = 0
score = 0
level = 1
power = 0

# -------------------------------------------
# TK WINDOW
# -------------------------------------------
root = tk.Tk()
root.title("Auto-Maze Pac-Man")
c = tk.Canvas(root, width=COLS*TILE, height=ROWS*TILE, bg="black")
c.pack()

# -------------------------------------------
# DRAW
# -------------------------------------------
def draw():
    c.delete("all")

    for r in range(ROWS):
        for col in range(COLS):
            tile = grid[r][col]
            x = col*TILE
            y = r*TILE

            if tile == "#":
                c.create_rectangle(x,y,x+TILE,y+TILE,fill=WALL,width=0)
            elif tile == ".":
                c.create_oval(x+9,y+9,x+15,y+15,fill=COIN,width=0)
            elif tile == "o":
                c.create_oval(x+6,y+6,x+18,y+18,fill=COIN,width=0)

    g_col = VULNERABLE if power > 0 else GHOST_COLOR
    c.create_oval(gx*TILE+2, gy*TILE+2, gx*TILE+TILE-2, gy*TILE+TILE-2, fill=g_col)
    c.create_oval(px*TILE+2, py*TILE+2, px*TILE+TILE-2, py*TILE+TILE-2, fill=PLAYER_COLOR)

    c.create_text(60, 10, fill="white", text=f"Score: {score}")
    c.create_text(180, 10, fill="white", text=f"Level: {level}")

# -------------------------------------------
# HELPERS
# -------------------------------------------
def free(x,y):
    if 0 <= x < COLS and 0 <= y < ROWS:
        return grid[y][x] != "#"
    return False

def dist(a,b,c,d):
    return abs(a-c)+abs(b-d)

# -------------------------------------------
# PLAYER
# -------------------------------------------
def move_player():
    global px, py, score, power, level

    nx = px + dir_x
    ny = py + dir_y

    if free(nx, ny):
        px, py = nx, ny

        # Coin
        if grid[py][px] == ".":
            grid[py][px] = " "
            score += 1

        # Power pellet
        if grid[py][px] == "o":
            grid[py][px] = " "
            power = 45

    # Level up
    if score >= level * 25:
        level += 1

# -------------------------------------------
# GHOST
# -------------------------------------------
def move_ghost():
    global gx, gy, score, power, px, py

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    options = []

    # Chase player when close & player NOT powered
    if dist(px, py, gx, gy) <= CHASE_RANGE and power == 0:
        best_d = 999
        for dx,dy in dirs:
            nx, ny = gx+dx, gy+dy
            if free(nx, ny):
                d = dist(nx, ny, px, py)
                if d < best_d:
                    best_d = d
                    options = [(nx, ny)]
                elif d == best_d:
                    options.append((nx, ny))
    else:
        # Wander
        for dx,dy in dirs:
            nx, ny = gx+dx, gy+dy
            if free(nx, ny):
                options.append((nx, ny))

    if options:
        gx, gy = random.choice(options)

    # Collision
    if gx == px and gy == py:
        if power > 0:
            gx, gy = ROWS-2, COLS-2
            score += 10
        else:
            reset_game()

# -------------------------------------------
# RESET
# -------------------------------------------
def reset_game():
    global px, py, gx, gy, dir_x, dir_y, level, score, power, grid
    px, py = 1, 1
    gx, gy = ROWS-2, COLS-2
    dir_x = dir_y = 0
    power = 0
    score = 0
    level = 1
    grid = generate_maze(ROWS)

# -------------------------------------------
# GAME LOOP
# -------------------------------------------
def loop():
    global power

    move_player()
    move_ghost()

    if power > 0:
        power -= 1

    draw()
    root.after(SPEED, loop)

# -------------------------------------------
# CONTROLS
# -------------------------------------------
def key(e):
    global dir_x, dir_y
    if e.keysym == "Up": dir_x, dir_y = 0, -1
    if e.keysym == "Down": dir_x, dir_y = 0, 1
    if e.keysym == "Left": dir_x, dir_y = -1, 0
    if e.keysym == "Right": dir_x, dir_y = 1, 0

root.bind("<Key>", key)

draw()
loop()
root.mainloop()
