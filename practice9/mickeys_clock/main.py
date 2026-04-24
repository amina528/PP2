import pygame
import sys
from clock import MickeyClock

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
mickey = MickeyClock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    mickey.draw(screen)

    pygame.display.flip()
    clock.tick(1)

pygame.quit()
sys.exit()