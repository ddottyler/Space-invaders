import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images

RED_SPACE_SHIPS = pygame.image.load(
    os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIPS = pygame.image.load(
    os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIPS = pygame.image.load(
    os.path.join("assets", "pixel_ship_blue_small.png"))

# Player ship
YELLOW_SPACE_SHIPS = pygame.image.load(
    os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_yellow.png"))

# Background

BG = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

# Abstract class. Won't be used, but we will inherit from it (enemy SHIP, player SHIP etc)


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0


def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        #  draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (0, 0, 225))
        WIN.blit(lives_label, (10, 10))
        # Line below has been written dynamically. WIN width and height can be changed and this will still work
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


main()
