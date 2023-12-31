import pygame
import random
import matplotlib.pyplot as plt
import numpy as np
from perlin_noise import PerlinNoise
import entities
from data import *

pygame.init()
PREY_POP = 1000
PRED_POP = 100
VEGETATION_POP = 1000
SEA_LEVEL = 0

GRID_SIZE_X = 100
GRID_SIZE_Y = 100
SEED_GEN = random.randint(0, 100)
NOISE = PerlinNoise(octaves=10, seed=SEED_GEN)
NOISE_GRID = [[NOISE([i/GRID_SIZE_X, j/GRID_SIZE_Y])+0.25 for i in range(GRID_SIZE_X)] for j in range(GRID_SIZE_Y)]
TILE_GRID = [[0 for i in range(GRID_SIZE_X)] for j in range(GRID_SIZE_Y)]


class BackgroundTile:
    def __init__(self, xpos, ypos):
        self.xsize = 5
        self.ysize = 5
        self.xpos = xpos
        self.ypos = ypos
        self.x = xpos * self.xsize
        self.y = ypos * self.ysize
        self.color = "azure"
        self.rect = None
        self.type = None
        self.make_rect()
        self.set_type()

    def make_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)

    def make_border(self):
        self.color = "gray43"
        self.type = "Border"

    def set_type(self):
        zHeight = NOISE_GRID[self.xpos][self.ypos]

        if zHeight > SEA_LEVEL + 0.1:
            self.color = "chartreuse4"
            self.type = "Grass"
        elif zHeight > SEA_LEVEL + 0.05:
            self.color = "lemonchiffon"
            self.type = "Sand"
        else:
            self.color = "cornflowerblue"
            self.type = "Water"


def make_background():
    for i in range(GRID_SIZE_X):
        for j in range(GRID_SIZE_Y):
            tile = BackgroundTile(i, j)
            TILE_GRID[i][j] = tile

            if i == 0 or i == GRID_SIZE_Y-1:
                tile.make_border()

            if j == 0 or j == GRID_SIZE_X-1:
                tile.make_border()

            if tile.type == "Grass":
                SPAWNABLE_TILES.append(tile)


def spawn_entities():
    for i in range(PRED_POP):
        pred = entities.Predators(4, "orangered3")  # Size, color

    for j in range(PREY_POP):
        prey = entities.Prey(3, "peru")  # Size, color

    for v in range(VEGETATION_POP):
        grass = entities.Grass()


make_background()
spawn_entities()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("azure")

    for i in range(GRID_SIZE_X):
        for j in range(GRID_SIZE_Y):
            pygame.draw.rect(screen, TILE_GRID[i][j].color, TILE_GRID[i][j])

    for a in ANIMALS:
        pygame.draw.rect(screen, a.color, a.rect)
        a.determine_priority()

    for g in VEGETATION:
        pygame.draw.rect(screen, g.color, g.rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
