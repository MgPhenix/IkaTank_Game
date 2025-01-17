from pygame import*

class Sanae(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.maxhp = 100
        self.attack = 10
        self.image = image.load("ProjetIkaMusume/assets/sanae1.png")
        self.rect = self.image.get_rect()

MangaPark
