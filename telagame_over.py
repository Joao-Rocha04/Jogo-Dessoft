from utilidade_tela import tela_generica
from assets import SOM_GAME_OVER
from config import IMG, QUIT, INIT
import pygame

def game_over_screen(tela):
    font = pygame.font.SysFont(None, 48)
    with open('score.py', 'r') as arquivo:
        score = arquivo.read()

    text = font.render(f'Você fez {int(score)} pontos!', True, (255, 255, 0))

    def additional_draws(s):
        s.blit(text, (330, 400))

    key_actions = {
        pygame.K_ESCAPE: INIT
    }

    return tela_generica(tela, 'Game_over.png', SOM_GAME_OVER, key_actions, additional_draws)
