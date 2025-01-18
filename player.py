from pygame import*
from projectile import Ink


class Player(sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.hp = 100
        self.maxhp = 100
        self.attack = 5
        self.all_projectiles = sprite.Group()
        self.image = image.load("ProjetIkaMusume/assets/ikatank.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 450
        self.speed = 1
    
    def damage(self, dgt):
        if self.hp - dgt > dgt:
            self.hp -= dgt
        else:
            self.game.game_over()



    def update_hp_bar(self, surface):
        draw.rect(surface, (60,63,60), [self.rect.x+75, self.rect.y-15, self.maxhp*2, 5])
        draw.rect(surface, (111,206,46), [self.rect.x+75, self.rect.y-15, self.hp*2, 5])
        

    def launch_ink(self):
        self.all_projectiles.add(Ink(self))

    
    def avancerD(self):
        if not self.game.check_collision(self, self.game.all_sanae):
            self.rect.x += self.speed
    
    def avancerG(self):
        self.rect.x -= self.speed
    