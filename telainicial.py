import pygame
from os import path
from assets import SOM_ENTRADA,load_assets
from config import IMG, preto, fps, GAME, QUIT, CONFIG



def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG, 'inicio.jpg')).convert()
    background = pygame.transform.scale(background,(1000,600))
    background_rect = background.get_rect()
    assets=load_assets()
    running = True
    while running:
        assets[SOM_ENTRADA].play(-1)
        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.KEYDOWN:
                

                if event.key == pygame.K_SPACE:
                    state = GAME
                    running = False
                
                if event.key ==pygame.K_w:
                    state = CONFIG
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(preto)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
