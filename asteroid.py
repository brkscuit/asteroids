import pygame
from circleshape import CircleShape
import random
from constants import * 

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        position = self.position
        pygame.draw.circle(screen, "white", position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if self.radius < ASTEROID_MIN_RADIUS:
            return
            
        #spawn new asteroids
        random_angle = random.uniform(20, 50)
        v1 = pygame.Vector2(self.velocity).rotate(random_angle)
        v2 = pygame.Vector2(self.velocity).rotate(-1 * random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        a1.velocity = v1 * 1.2
        a2.velocity = v2
        
        
    
