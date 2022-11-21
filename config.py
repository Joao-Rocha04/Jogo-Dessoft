from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
#SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
#FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
largura = 600 # Largura da tela
altura = 600 # Altura da tela
fps = 60 # Frames por segundo

# Define tamanhos
# Define tamanhos
largura_inimigo1 = 20
altura_inimigo1 = 35

largura_inimigo2 = 20
altura_inimigo2 = 35

largura_inimigo3 = 30
altura_inimigo3 = 50

largura_inimigo4 = 30
altura_inimigo4 = 50

largura_inimigo5 = 35
altura_inimigo5 = 60

largura_principal = 30
altura_principal = 40

# Define algumas variáveis com as cores básicas
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2