import pygame
from data import *
import random


class Entity:
    def __init__(self):
        self.x = random.randint(1, 500)
        self.y = random.randint(1, 500)


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
        self.hunger = 0
        self.thirst = 0
        self.urge = 0
        self.speed = 0

    def set_stats(self):
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

