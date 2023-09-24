import pygame
from data import *
import random

SPAWNABLE_TILE_COUNT = len(SPAWNABLE_TILES)

class Entity:
    def __init__(self):
        spawn_tile = SPAWNABLE_TILES[random.randint(0, len(SPAWNABLE_TILES)-1)]
        self.x = spawn_tile.x + random.randint(0, spawn_tile.xsize-2)
        self.y = spawn_tile.y + random.randint(0, spawn_tile.ysize-2)


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
        self.dir = 0  # Eight possible directions (from diagonal up-left to diagonal down-right
        # 0 Entails no direction
        self.dirPreference = 0  # How likely an animal will keep their direction

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

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def wander(self):
        # Move randomly until priority is within range
        if self.dir == 0 or self.dirPreference == 0:
            self.dir = random.randint(1, 8)
            self.dirPreference = random.randint(50, 150)

        if self.dir == 1:
            self.x -= 1  # * speed * dt
            self.y += 1  # * speed * dt
        elif self.dir == 2:
            self.y += 1  # * speed * dt
        elif self.dir == 3:
            self.x += 1  # * speed * dt
            self.y += 1  # * speed * dt
        elif self.dir == 4:
            self.x -= 1  # * speed * dt
        elif self.dir == 5:
            self.x += 1  # * speed * dt
        elif self.dir == 6:
            self.x -= 1  # * speed * dt
            self.y -= 1  # * speed * dt
        elif self.dir == 7:
            self.y -= 1  # * speed * dt
        elif self.dir == 8:
            self.x += 1  # * speed * dt
            self.y -= 1  # * speed * dt

        self.update_rect()
        self.dirPreference -= 1

    def mate(self):
        return

    def birth(self):
        return

    def determine_priority(self):
        self.approach_priority()

    def approach_priority(self):
        # set new dir and reset dirpreference
        self.wander()


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

    def escape_predator(self):
        return

class Rabbit(Prey):
    def __init__(self, size, color):
        super().__init__(size, color)


class Fox(Predators):
    def __init__(self, size, color):
        super().__init__(size, color)

