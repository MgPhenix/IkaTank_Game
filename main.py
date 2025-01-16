from pygame import* 
from game import Game

init()
display.set_caption("Ika Musume Game Degeso")
fond = image.load("ProjetIkaMusume/assets/background.png")




game = Game()



fini = False
while not fini:
    game.screen.blit(fond, (0, 0))
    game.screen.blit(game.player1.image, game.player1.rect)
    for projectile in game.player1.all_projectiles:
        projectile.move()
    game.player1.all_projectiles.draw(game.screen)
    if game.pressed.get(K_RIGHT):# and game.player1.rect.x + game.player1.rect.width < 1280:
        game.player1.avancerD() 
    elif game.pressed.get(K_LEFT):# and game.player1.rect.x > 0:
        game.player1.avancerG()


    display.flip()
    for evenement in event.get():
        if evenement.type == QUIT:
            fini = True
        elif evenement.type == KEYDOWN:
            game.pressed[evenement.key] = True

            if evenement.key == K_SPACE:
                game.player1.launch_ink()
        elif evenement.type == KEYUP:
            game.pressed[evenement.key] = False



