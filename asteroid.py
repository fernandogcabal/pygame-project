import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pos = (int(self.position.x), int(self.position.y))
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, pos, int(self.radius), LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if (self.radius <= ASTEROID_MIN_RADIUS):
             return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = vel1 * 1.2
        a2.velocity = vel2 * 1.2
