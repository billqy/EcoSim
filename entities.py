import pygame
from data import *
import random

SPAWNABLE_TILE_COUNT = len(SPAWNABLE_TILES)

class Entity:
    def __init__(self):
        spawn_tile = SPAWNABLE_TILES[random.randint(0, len(SPAWNABLE_TILES)-1)]
        self.x = spawn_tile.x + random.randint(1, spawn_tile.xsize-2)
        self.y = spawn_tile.y + random.randint(1, spawn_tile.ysize-2)


class Grass(Entity):
    def __init__(self):
        super().__init__()
        VEGETATION.append(self)
        self.size = 2
        self.color = "darkgreen"
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)


class Animals(Entity):
    def __init__(self, size, color):
        super().__init__()
        self.size = size
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

        self.sex = None
        self.energy = 0
        self.water = 0
        self.urge = 0

        self.range = 0
        self.speed = 0

    def set_stats(self):
        return

    def update_stats(self):
        return

    def wander(self):
        return

    def determine_priority(self):
        return


class Predators(Animals):
    def __init__(self, size, color):
        super().__init__(size, color)
        ANIMALS.append(self)
        PREDATORS.append(self)


class Prey(Animals):
    def __init__(self, size, color):
        super().__init__(size, color)
        ANIMALS.append(self)
        PREY.append(self)


class Rabbit(Prey):
    def __init__(self, size, color):
        super().__init__(size, color)


class Fox(Predators):
    def __init__(self, size, color):
        super().__init__(size, color)

