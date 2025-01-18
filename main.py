from pygame import* 
from game import Game

init()
display.set_caption("Ika Musume Game Degeso")
fond = image.load("ProjetIkaMusume/assets/background.png")
logo = image.load("ProjetIkaMusume/assets/logo.png")
#logo = transform.scale(logo, (400,400))
button = image.load("ProjetIkaMusume/assets/play.png")
button_rect = button.get_rect()
button_rect.x = 460
button_rect.y = 500
font.init()

game = Game()



run = True
while run:
    game.screen.blit(fond, (0, 0))
    
    if game.is_playing:
        game.update()
    else:
        game.screen.blit(logo, (300, 70))
        game.screen.blit(button, button_rect)

    display.flip()
    for evenement in event.get():
        if evenement.type == QUIT:
            run = False
        elif evenement.type == KEYDOWN:
            game.pressed[evenement.key] = True

            if evenement.key == K_SPACE:
                game.player1.launch_ink()
        elif evenement.type == KEYUP:
            game.pressed[evenement.key] = False
        elif evenement.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(evenement.pos):
                game.start()


