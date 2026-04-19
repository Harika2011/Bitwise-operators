import pygame
import random
import sys
import time

# Initialize
pygame.init()

# Screen setup
WIDTH, HEIGHT = 900, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
LIGHT_GREEN = (120, 255, 120)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
PURPLE = (180, 0, 255)
ORANGE = (255, 140, 0)
GREY = (40, 40, 40)
DARK_GREY = (20, 20, 20)
BLUE = (0, 180, 255)

# Fonts
font_big = pygame.font.SysFont("comicsansms", 52, bold=True)
font_med = pygame.font.SysFont("comicsansms", 30)
font_small = pygame.font.SysFont("arial", 20)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Evolution: Adventure")

# Clock
clock = pygame.time.Clock()

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# ================= Helper Functions =================

def draw_text(text, color, x, y, font=font_small, center=False):
    label = font.render(text, True, color)
    if center:
        rect = label.get_rect(center=(x, y))
        screen.blit(label, rect)
    else:
        screen.blit(label, (x, y))


def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, DARK_GREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, DARK_GREY, (0, y), (WIDTH, y))


def random_position():
    return [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]


def draw_snake(snake):
    for i, segment in enumerate(snake):
        r = (i * 5) % 255
        g = 255 - (i * 3) % 255
        b = (i * 7) % 255
        color = (r, g, b)
        pygame.draw.rect(screen, color, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, BLACK, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


def draw_food(food, type="normal", blink=False):
    if type == "normal":
        color = RED if blink else ORANGE
    elif type == "bonus":
        color = LIGHT_GREEN
    else:  # poison
        color = PURPLE
    pygame.draw.circle(screen, color, (food[0]*CELL_SIZE + CELL_SIZE//2, food[1]*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//2)


def draw_obstacles(obstacles):
    for obs in obstacles:
        pygame.draw.rect(screen, GREY, (obs[0]*CELL_SIZE, obs[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, BLACK, (obs[0]*CELL_SIZE, obs[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


# ================= Menus =================

def start_menu():
    blink = True
    while True:
        screen.fill(BLACK)
        draw_text("🐍 Snake Evolution 🐍", YELLOW, WIDTH // 2, HEIGHT // 3, font_big, center=True)
        if blink:
            draw_text("Press ENTER to Start", GREEN, WIDTH // 2, HEIGHT // 2, font_med, center=True)
        draw_text("Press ESC to Quit", WHITE, WIDTH // 2, HEIGHT // 2 + 60, font_small, center=True)
        pygame.display.flip()
        blink = not blink
        clock.tick(2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    instructions_menu()
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def instructions_menu():
    blink = True
    while True:
        screen.fill(BLACK)
        draw_text("📜 Instructions 📜", YELLOW, WIDTH // 2, 60, font_big, center=True)
        draw_text("Controls:", WHITE, WIDTH // 2 - 250, 130)
        draw_text("Arrow Keys → Move the snake", WHITE, WIDTH // 2 - 200, 160)
        draw_text("P → Pause / Resume", WHITE, WIDTH // 2 - 200, 190)
        draw_text("ESC → Quit Game", WHITE, WIDTH // 2 - 200, 220)

        draw_text("Gameplay:", WHITE, WIDTH // 2 - 250, 260)
        draw_text("• Eat RED food → +10 points", RED, WIDTH // 2 - 200, 290)
        draw_text("• Eat GREEN food → +30 points (Bonus!)", LIGHT_GREEN, WIDTH // 2 - 200, 320)
        draw_text("• Avoid PURPLE food → -15 points", PURPLE, WIDTH // 2 - 200, 350)
        draw_text("• Hitting obstacles or walls → Game Over", GREY, WIDTH // 2 - 200, 380)

        draw_text("• Snake grows longer with each food eaten", WHITE, WIDTH // 2 - 200, 420)
        draw_text("• Levels increase every 70 points → Speed Up!", WHITE, WIDTH // 2 - 200, 450)
        if blink:
            draw_text("Press ENTER to Begin Your Adventure!", GREEN, WIDTH // 2, HEIGHT - 80, font_med, center=True)

        pygame.display.flip()
        blink = not blink
        clock.tick(2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return


def pause_menu():
    paused = True
    while paused:
        draw_text("⏸ Paused ⏸", BLUE, WIDTH // 2, HEIGHT // 2 - 40, font_big, center=True)
        draw_text("Press P to Resume or ESC to Quit", WHITE, WIDTH // 2, HEIGHT // 2 + 20, font_med, center=True)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def game_over_menu(score):
    blink = True
    while True:
        screen.fill(BLACK)
        draw_text("💀 GAME OVER 💀", RED, WIDTH // 2, HEIGHT // 3, font_big, center=True)
        draw_text(f"Final Score: {score}", YELLOW, WIDTH // 2, HEIGHT // 2, font_med, center=True)
        if blink:
            draw_text("Press ENTER to Restart or ESC to Quit", WHITE, WIDTH // 2, HEIGHT // 2 + 60, font_small, center=True)
        pygame.display.flip()
        blink = not blink
        clock.tick(2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


# ================= Main Game =================

def main():
    start_menu()

    snake = [[10, 10], [9, 10], [8, 10]]
    direction = RIGHT
    score = 0
    level = 1
    speed = 10
    blink = True

    food = random_position()
    bonus_food = None
    poison_food = None
    obstacles = []

    game_over = False

    while True:
        screen.fill(BLACK)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT
                elif event.key == pygame.K_p:
                    pause_menu()

        if not game_over:
            new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
            snake.insert(0, new_head)

            if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
                game_over = True

            if new_head in snake[1:] or new_head in obstacles:
                game_over = True

            if new_head == food:
                score += 10
                food = random_position()
                if random.random() < 0.15:
                    bonus_food = random_position()
                if random.random() < 0.10:
                    poison_food = random_position()
                if score % 70 == 0:
                    level += 1
                    speed += 1
                    for _ in range(3):
                        obstacles.append(random_position())
            elif bonus_food and new_head == bonus_food:
                score += 30
                bonus_food = None
            elif poison_food and new_head == poison_food:
                score -= 15
                poison_food = None
                if len(snake) > 3:
                    snake.pop()
                    snake.pop()
            else:
                snake.pop()

        draw_snake(snake)
        draw_food(food, "normal", blink)
        if bonus_food:
            draw_food(bonus_food, "bonus")
        if poison_food:
            draw_food(poison_food, "poison")
        draw_obstacles(obstacles)
        blink = not blink

        pygame.draw.rect(screen, DARK_GREY, (0, 0, WIDTH, 40))
        draw_text(f"Score: {score}", YELLOW, 20, 10)
        draw_text(f"Level: {level}", LIGHT_GREEN, 200, 10)
        draw_text(f"Length: {len(snake)}", BLUE, 340, 10)
        draw_text("Press P to Pause", WHITE, WIDTH - 180, 10)

        if score < 50:
            msg = "Keep going, you're learning control!"
        elif score < 150:
            msg = "🔥 Great reflexes! Level up!"
        else:
            msg = "🏆 Master snake in action!"
        draw_text(msg, ORANGE, WIDTH // 2 - 150, HEIGHT - 30)

        if game_over:
            draw_text("💥 You Crashed! 💥", RED, WIDTH // 2, HEIGHT // 2 - 20, font_med, center=True)
            pygame.display.flip()
            time.sleep(2)
            game_over_menu(score)

        pygame.display.flip()
        clock.tick(speed)


if __name__ == "__main__":
    main()
