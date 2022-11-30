# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import INIT, GAME, QUIT, CONFIG, OVER
from telainicial import init_screen
from Principal import game_screen
from telaconfig import config_screen
from telagame_over import game_over_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Barbara s Adventure')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == CONFIG:
        state = config_screen(window)
    elif state == OVER:
        state = game_over_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

