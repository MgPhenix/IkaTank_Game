from pygame import* 
from player import Player
from sanae import Sanae

font.init()
my_font = font.SysFont('Comic Sans MS', 40)


class Game:
    def __init__(self):
        self.is_playing = False
        self.screen = display.set_mode((1280,720))
        self.score = 0
        self.player1 = Player(self)
        self.all_sanae = sprite.Group()
        self.all_players = sprite.Group()
        self.all_players.add(self.player1)
        self.pressed = {}
        self.crevette = image.load("ProjetIkaMusume/assets/crevette.png")
        self.crevette = transform.scale(self.crevette, (50,50))   
        self.crevette_rect = self.crevette.get_rect()
        self.crevette_rect.x = 60
        self.crevette_rect.y = 0
        self.perdu = image.load("ProjetIkaMusume/assets/perdu.png")
        #self.spawn_sanae()
        #self.spawn_sanae()

    def start(self):
        self.is_playing = True
        self.spawn_sanae()
        self.spawn_sanae()

    def game_over(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.perdu, (350,200))
        text = my_font.render(f"Final Score : {str(self.score)}", False, (255,255,255))
        self.screen.blit(text, (480,400))
        display.flip()
        time.delay(6000)
        self.score = 0
        self.all_sanae = sprite.Group()
        self.player1.hp = self.player1.maxhp
        self.is_playing = False

    def update(self):
        self.screen.blit(self.player1.image, self.player1.rect)
        self.all_sanae.draw(self.screen)
        self.player1.update_hp_bar(self.screen)
        self.screen.blit(self.crevette, self.crevette_rect)
        text = my_font.render(str(self.score), False, (255,255,255))
        self.screen.blit(text, (20,0))
        for sanae in self.all_sanae:
            sanae.forward()
            sanae.update_hp_bar(self.screen)
        for projectile in self.player1.all_projectiles:
            projectile.move()
        self.player1.all_projectiles.draw(self.screen)
        if self.pressed.get(K_RIGHT):# and self.player1.rect.x + self.player1.rect.width < 1280:
            self.player1.avancerD() 
        elif self.pressed.get(K_LEFT):# and self.player1.rect.x > 0:
            self.player1.avancerG()


    def check_collision(self, sprite1, group):
        return sprite.spritecollide(sprite1, group, False, sprite.collide_mask)

    def spawn_sanae(self):
        sanae = Sanae(self)
        self.all_sanae.add(sanae)

    