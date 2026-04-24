import pygame
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Moving Ball")

ball = Ball()

running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            ball.move(event.key)

    screen.fill((255,255,255))
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()