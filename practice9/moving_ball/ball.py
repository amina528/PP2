import pygame

class Ball:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.radius = 25
        self.speed = 20

    def move(self, key):
        if key == pygame.K_LEFT:
            self.x -= self.speed
        if key == pygame.K_RIGHT:
            self.x += self.speed
        if key == pygame.K_UP:
            self.y -= self.speed
        if key == pygame.K_DOWN:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255,0,0), (self.x,self.y), self.radius)