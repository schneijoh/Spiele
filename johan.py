import pygame
import random
import sys

# --------------------
# Initialisierung
# --------------------
pygame.init()
WIDTH, HEIGHT = 900, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wüstenläufer")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Farben (Schwarz / Weiß)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (120, 120, 120)

# --------------------
# Spieler
# --------------------
player_width = 40
player_height = 60
player_x = 100
player_y = HEIGHT - player_height - 40
player_vel_y = 0
gravity = 1
jump_strength = -18
on_ground = True

# --------------------
# Hindernisse (Bäume)
# --------------------
obstacles = []
obstacle_width = 30
obstacle_height = 70
obstacle_speed = 6
spawn_timer = 0

# --------------------
# Zeit
# --------------------
start_time = pygame.time.get_ticks()

def reset_game():
    global obstacles, player_y, player_vel_y, on_ground, start_time
    obstacles = []
    player_y = HEIGHT - player_height - 40
    player_vel_y = 0
    on_ground = True
    start_time = pygame.time.get_ticks()

# --------------------
# Hauptschleife
# --------------------
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # --------------------
    # Events
    # --------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                player_vel_y = jump_strength
                on_ground = False

    # --------------------
    # Spieler Physik
    # --------------------
    player_vel_y += gravity
    player_y += player_vel_y

    if player_y >= HEIGHT - player_height - 40:
        player_y = HEIGHT - player_height - 40
        player_vel_y = 0
        on_ground = True

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # --------------------
    # Hindernisse erzeugen
    # --------------------
    spawn_timer += 1
    if spawn_timer > 90:
        spawn_timer = 0
        obstacles.append(
            pygame.Rect(
                WIDTH,
                HEIGHT - obstacle_height - 40,
                obstacle_width,
                obstacle_height
            )
        )

    # --------------------
    # Hindernisse bewegen
    # --------------------
    for obstacle in obstacles:
        obstacle.x -= obstacle_speed

    obstacles = [o for o in obstacles if o.x > -50]

    # --------------------
    # Kollision
    # --------------------
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            reset_game()

    # --------------------
    # Zeichnen
    # --------------------

    # Boden
    pygame.draw.rect(screen, GRAY, (0, HEIGHT - 40, WIDTH, 40))

    # Spieler
    pygame.draw.rect(screen, BLACK, player_rect)

    # Bäume (Hindernisse)
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)  # Stamm
        pygame.draw.circle(
            screen,
            BLACK,
            (obstacle.centerx, obstacle.y),
            25
        )

    # Zeit anzeigen
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    time_text = font.render(f"Zeit: {elapsed_time}s", True, BLACK)
    screen.blit(time_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
