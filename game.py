from pygame import* 
from player import Player

class Game:
    def __init__(self):
        self.screen = display.set_mode((1280,720))
        self.score = 0
        self.player1 = Player(self)
        #self.all_players = sprite.Group()
        #self.all_players.add(self.player1)
        self.pressed = {}