import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	
	
	print("Starting Asteroids!",
	   "Screen width: 1280",
	   "Screen height: 720")
	
	all_shots = []
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		player.update(dt, all_shots)
		updatable.update(dt)
		for asteroid in asteroids:
			if player.is_colliding(asteroid):
				print("GAME OVER!")
				sys.exit()
		
		screen.fill((0, 0, 0))
		for drawable_sprite in drawable:
			drawable_sprite.draw(screen)
		for shot in all_shots:
			shot.draw(screen)
		
		pygame.display.flip()
		dt = clock.tick(60) / 1000

		for shot in all_shots:
			shot.update(dt)
			if not shot.is_alive:
				all_shots.remove(shot)

if __name__ == "__main__":
	main()