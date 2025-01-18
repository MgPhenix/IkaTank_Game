from pygame import*
from random import randint

class Sanae(sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.hp = 100
        self.maxhp = 100
        self.attack = 0.05
        self.image = image.load("ProjetIkaMusume/assets/sanae1.png")
        self.image = transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + randint(0,200)
        self.rect.y = 450
        self.speed = randint(1,1)

    def damage(self, dgt):
        self.hp -= dgt
        self.rect.x += 10
        if self.hp <= 0:    
            #self.remove()
            self.rect.x = 1000 + randint(0,200)
            self.hp = self.maxhp
            self.speed = randint(1,1)
            self.game.score += 1

    def update_hp_bar(self, surface):
        draw.rect(surface, (60,63,60), [self.rect.x+25, self.rect.y, self.maxhp, 5])
        draw.rect(surface, (111,206,46), [self.rect.x+25, self.rect.y, self.hp, 5])
        

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players): #or not self.game.check_collision(self, self.game.all_sanae):
            self.rect.x -= self.speed
        
        else:
            self.game.player1.damage(self.attack)




#MangaPark
#I admire magical girl...