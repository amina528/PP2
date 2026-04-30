import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

x, y = WIDTH // 2, HEIGHT // 2
radius = 25
speed = 20

running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                if x - radius - speed >= 0:
                    x -= speed

            if event.key == pygame.K_RIGHT:
                if x + radius + speed <= WIDTH:
                    x += speed

            if event.key == pygame.K_UP:
                if y - radius - speed >= 0:
                    y -= speed

            if event.key == pygame.K_DOWN:
                if y + radius + speed <= HEIGHT:
                    y += speed

    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.flip()

pygame.quit()
sys.exit()