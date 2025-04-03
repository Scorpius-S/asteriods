import pygame
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS, SHOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius, speed, direction, color=(255, 255, 255)):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, -1).rotate(direction) * speed
        self.color = color
        self.is_alive = True

    def update(self, dt):
        self.position += self.velocity * dt
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or 
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.is_alive = False
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

