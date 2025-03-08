from circleshape import CircleShape
from constants import *
import pygame
import random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
        
    def update(self, dt):
        # Move the asteroid based on its velocity and time passed
        self.position += self.velocity * dt
    def split(self):
        # Split the asteroid into two smaller asteroids
        self.kill()
        spawn_angle = random.uniform(20, 50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            velocity1 = self.velocity.rotate(spawn_angle)
            velocity2 = self.velocity.rotate(- spawn_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = velocity2 * 1.2

