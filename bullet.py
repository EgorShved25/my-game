import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' Класс для управления снарядами текущей позиции коробля.'''

    def __init__(self, ai_game):
        '''Создает обьект снарядов в текущей позиции корабля.'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд вверх по экрану."""

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        self.screen.blit(self.image, self.rect)