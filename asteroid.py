import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        self.position = pygame.Vector2(x, y)
        self.radius = radius

        if velocity is None:
            angle = random.uniform(0, 360)
            speed = random.uniform(50, 100)
            self.velocity = pygame.Vector2(speed, 0).rotate(angle)
        else:
            self.velocity = velocity

        super().__init__(x, y, radius)


    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(random_angle) * 1.1
            new_velocity2 = self.velocity.rotate(-random_angle) * 1.1
            offset_distance = self.radius / 2
            offset1 = new_velocity1.normalize() * offset_distance
            offset2 = new_velocity2.normalize() * offset_distance
            asteroid1 = Asteroid(self.position.x + offset1.x, self.position.y + offset1.y, new_radius, new_velocity1)
            asteroid2 = Asteroid(self.position.x + offset2.x, self.position.y + offset2.y, new_radius, new_velocity2)
            return asteroid1, asteroid2

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
