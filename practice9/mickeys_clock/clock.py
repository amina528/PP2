import pygame
import datetime

class MickeyClock:
    def __init__(self):
        self.clock_img = pygame.image.load("images/clock.png")
        self.clock_img = pygame.transform.scale(self.clock_img, (600, 600))

        # ❗ НЕ уменьшай слишком сильно
        self.minute_hand = pygame.image.load("images/minute_hand.png")
        self.second_hand = pygame.image.load("images/second_hand.png")

        # нормальный размер (важно!)
        self.minute_hand = pygame.transform.scale(self.minute_hand, (20, 220))
        self.second_hand = pygame.transform.scale(self.second_hand, (10, 260))

        self.center = (300, 300)

    def draw(self, screen):
        screen.blit(self.clock_img, (0, 0))

        now = datetime.datetime.now()

        sec_angle = -now.second * 6
        min_angle = -now.minute * 6

        # rotate (после scale)
        sec_rot = pygame.transform.rotate(self.second_hand, sec_angle)
        min_rot = pygame.transform.rotate(self.minute_hand, min_angle)

        sec_rect = sec_rot.get_rect(center=self.center)
        min_rect = min_rot.get_rect(center=self.center)

        # важно: порядок
        screen.blit(min_rot, min_rect)
        screen.blit(sec_rot, sec_rect)