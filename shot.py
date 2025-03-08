from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    containers = None
    
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS
        self.velocity = velocity
        if Shot.containers:
            for container in Shot.containers:
                container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        # Move the shot based on its velocity and the time passed
        self.position += self.velocity * dt