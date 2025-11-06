from circleshape import CircleShape
import pygame
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, (255, 255, 255), center, int(self.radius), 2)
    def update(self, dt):
        self.position += self.velocity * dt
