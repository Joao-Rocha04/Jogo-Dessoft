from utilidade_tela import tela_generica
from assets import SOM_ENTRADA
from config import IMG, GAME, QUIT, CONFIG
import pygame

def init_screen(tela):
    def additional_draws(s):
        pass

    key_actions = {
        pygame.K_SPACE: GAME,
        pygame.K_w: CONFIG
    }

    return tela_generica(tela, 'inicio1.png', SOM_ENTRADA, key_actions, additional_draws)
