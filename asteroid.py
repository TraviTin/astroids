from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, (255, 255, 255), center, int(self.radius), 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        Asteroid.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = velocity2 * 1.2    