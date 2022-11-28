import pygame
from os import path
from assets import load_assets,SOM_GAME_OVER
from config import IMG, preto, fps,QUIT,INIT


def game_over_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG, 'Game_over.png')).convert()
    background = pygame.transform.scale(background,(1000,600))
    background_rect = background.get_rect()
    assets[SOM_GAME_OVER].play()
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.KEYDOWN:
                

                if event.key == pygame.K_ESCAPE:
                    state = INIT
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(preto)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state