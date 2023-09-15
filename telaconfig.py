from utilidade_tela import tela_generica
from assets import SOM_ENTRADA
from config import IMG, QUIT, INIT
import pygame

def config_screen(screen):
    def additional_draws(s):
        pass

    key_actions = {
        pygame.K_ESCAPE: INIT
    }

    return tela_generica(screen, 'config.jpg', SOM_ENTRADA, key_actions, additional_draws)
