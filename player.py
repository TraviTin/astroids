from circleshape import CircleShape
import pygame
from constants import *
from shot import Shot



class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots =shots_group
        self.timer = 0
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    # in the player class
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)  
        if keys[pygame.K_d]:
            self.rotate(dt)  
        if keys[pygame.K_SPACE]:
            self.shoot()
        if self.timer > 0:
            self.timer = max((self.timer-dt), 0)
    def shoot(self):
        if self.timer > 0:
            return
        v = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        s = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        s.velocity = v
        self.shots.add(s)
        self.timer = PLAYER_SHOOT_COOLDOWN
        
