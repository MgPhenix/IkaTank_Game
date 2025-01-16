from pygame import*
from projectile import Ink

class Player(sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.hp = 3
        self.all_projectiles = sprite.Group()
        self.image = image.load("ProjetIkaMusume/assets/ikatank.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 450
        self.speed = 1

    def launch_ink(self):
        self.all_projectiles.add(Ink(self))

    
    def avancerD(self):
        self.rect.x += self.speed
    
    def avancerG(self):
        self.rect.x -= self.speed
    