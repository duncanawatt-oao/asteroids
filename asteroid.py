from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self,x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_ang = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_velocity_1 = self.velocity.rotate(new_ang) * 1.2
        new_velocity_2 = self.velocity.rotate(-new_ang) * 1.2

        new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_1.velocity = new_velocity_1
        
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_2.velocity = new_velocity_2
