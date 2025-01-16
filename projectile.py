from pygame import *


class Ink(sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.speed = 2
        self.player = player
        self.image = image.load("ProjetIkaMusume/assets/ink.png")
        self.image = transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x +370
        self.rect.y = player.rect.y + 50
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 8
        self.image = transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.speed
        self.rotate()
        if self.rect.x > 1280:
            self.remove()