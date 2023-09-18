# Um arquivo comum, por exemplo: screen_utils.py

import pygame
from os import path
from config import preto, fps, QUIT
from assets import load_assets

def tela_generica(screen, background_img, sound_key, event_key_actions, additional_draws=None):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo
    background = pygame.image.load(path.join(IMG, background_img)).convert()
    background = pygame.transform.scale(background, (1000, 600))
    background_rect = background.get_rect()

    assets = load_assets()

    # Toca o som
    if sound_key:
        assets[sound_key].play(-1)

    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.stop(assets[sound_key])
                return QUIT
            
            if event.type == pygame.KEYDOWN:
                if event.key in event_key_actions:
                    pygame.mixer.Sound.stop(assets[sound_key])
                    return event_key_actions[event.key]

        # Desenha o fundo
        screen.fill(preto)
        screen.blit(background, background_rect)

        # Desenha elementos adicionais, se houver
        if additional_draws:
            additional_draws(screen)

        # Atualiza a tela
        pygame.display.flip()



from assets import SOM_ENTRADA
from config import IMG, GAME, QUIT, CONFIG

def init_screen(tela):
    def additional_draws(s):
        pass

    key_actions = {
        pygame.K_SPACE: GAME,
        pygame.K_w: CONFIG
    }

    return tela_generica(tela, 'inicio1.png', SOM_ENTRADA, key_actions, additional_draws)
