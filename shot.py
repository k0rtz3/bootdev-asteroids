import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.SHOT_RADIUS = SHOT_RADIUS 

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "red", (int(self.position.x), int(self.position.y)), self.SHOT_RADIUS, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt