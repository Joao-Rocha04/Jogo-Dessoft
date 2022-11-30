import pygame
from os import path
from assets import SOM_ENTRADA,load_assets
from config import IMG, preto, fps, GAME, QUIT, CONFIG



def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG, 'inicio1.png')).convert()
    background = pygame.transform.scale(background,(1000,600))
    background_rect = background.get_rect()
    assets=load_assets()
    running = True
    #toca o som de fundo e deixa em loop
    assets[SOM_ENTRADA].play(-1)
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                pygame.mixer.Sound.stop(assets[SOM_ENTRADA])
                running = False
            
            if event.type == pygame.KEYDOWN:
                

                if event.key == pygame.K_SPACE:
                    state = GAME
                    #Para o som caso troque a janela
                    pygame.mixer.Sound.stop(assets[SOM_ENTRADA])
                    running = False
                
                if event.key ==pygame.K_w:
                    state = CONFIG
                    #Para o som caso troca a janela
                    pygame.mixer.Sound.stop(assets[SOM_ENTRADA])
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(preto)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
