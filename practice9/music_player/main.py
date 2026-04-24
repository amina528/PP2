import pygame
from player import MusicPlayer

pygame.init()

screen = pygame.display.set_mode((600,400))
player = MusicPlayer()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            if event.key == pygame.K_s:
                player.stop()

            if event.key == pygame.K_n:
                player.next()

            if event.key == pygame.K_b:
                player.back()

            if event.key == pygame.K_q:   # ← добавили
                running = False

pygame.quit()