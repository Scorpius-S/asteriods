from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_SPEED, SHOT_RADIUS, SHOT_SPEED
import pygame
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.PLAYER_SHOOT_COOLDOWN = 0.3

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius  
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, all_shoots):
        forward = pygame.Vector2(0, -1).rotate(self.rotation) * self.radius
        shot_position = self.position + forward
        self.timer = self.PLAYER_SHOOT_COOLDOWN
        
        if all_shoots is None:
            print("Error: all_shoots is None")
            return
        
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED
        
        shot = Shot(
            x=shot_position.x,
            y=shot_position.y,
            radius=SHOT_RADIUS,
            color=(255, 255, 255),
            speed=SHOT_SPEED,
            direction=self.rotation
        )
        all_shoots.append(shot)
    

    def update(self, dt, all_shots=None):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_SPEED * dt
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if self.timer > 0:
            return
        if keys[pygame.K_SPACE]:
            self.shoot(all_shots)

            
        

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
