import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid  import Asteroid
from logger import log_state, log_event
from circleshape import CircleShape
import sys
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers= (updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, shots)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    break
        for asteroid in asteroids:
            if player.collision(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        log_state()
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
