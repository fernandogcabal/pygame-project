import pygame
from constants import LINE_WIDTH, SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # use the Vector2 position from CircleShape and a proper RGB color tuple
        pos = (int(self.position.x), int(self.position.y))
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, pos, SHOT_RADIUS, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt