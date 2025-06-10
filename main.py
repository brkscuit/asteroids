# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    #create player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()
    dt = 0
    
    #game loop
    while True:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        #draw screen
        screen.fill("black")
    
        updatable.update(dt)
        #Check for collisions
        for asteroid in asteroids:
            if player.isHit(asteroid):
                print("Game over!")
                return
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.isHit(shot):
                    asteroid.split()
                    shot.kill()
        
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        
        #draw screen at rate of 60 FPS
        dt = clock.tick(60) / 1000
                
        
if __name__ == "__main__":
    main()
