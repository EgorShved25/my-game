import pygame
from pygame.sprite import Sprite
import random


width = 1920
HEIGHT = 1080
class Alien(Sprite):
    ''' Класс, представляющий одного пришельца. '''

    def __init__(self, ai_game):
        '''"Инициализирует пришельца и задает его начальную позицию. '''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 9)
        self.speedx = random.randrange(-3, 3)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)



    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 100  or self.rect.left < -25 or self.rect.right > width + 200:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-200, -100)
            self.speedy = random.randrange(1, 8)