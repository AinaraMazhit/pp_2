import random
import pygame

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn_time = pygame.time.get_ticks()

    def respawn(self, snake_body):
        while True:
            x = random.randint(0, 29) * 20
            y = random.randint(0, 19) * 20
            if (x, y) not in snake_body:
                self.position = (x, y)
                self.spawn_time = pygame.time.get_ticks()  
                break
