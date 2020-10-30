import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 750, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images
R_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
G_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
B_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player ship
Y_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
R_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
G_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
B_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
Y_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")),(WIDTH, HEIGHT))


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = Y_SHIP
        self.laser_img = Y_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    COLOR_MAP = {
                "red": (R_SHIP, R_LASER),
                "green": (G_SHIP, G_LASER),
                "blue": (B_SHIP, B_LASER)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel


def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5

    player = Player(300, 450)

    clock = pygame.time.Clock()


    def redraw_window():
        WIN.blit(BG, (0,0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        font_size = 10

        WIN.blit(lives_label, (font_size, font_size))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - font_size, font_size))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)


        pygame.display.update()

    while run:
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player.get_width() < WIDTH:
            player.x += player_vel
        if keys[pygame.K_DOWN] and player.y + player.get_height() < HEIGHT:
            player.y += player_vel
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= player_vel

        for enemy in enemies:
            enemy.move(enemy_vel)

        redraw_window()

main()
