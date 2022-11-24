from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG = path.join(path.dirname(__file__), 'assets', 'img',)
#SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT = path.join(path.dirname(__file__), 'assets', 'fnt')

# Dados gerais do jogo.
largura = 1000 # Largura da tela
altura = 600 # Altura da tela
fps = 60 # Frames por segundo

# Define tamanhos
# Define tamanhos
largura_inimigo1 = 50
altura_inimigo1 = 50

largura_inimigo2 = 40
altura_inimigo2 = 50

largura_inimigo3 = 100
altura_inimigo3 = 110

largura_inimigo4 = 95
altura_inimigo4 = 90

largura_inimigo5 = 100
altura_inimigo5 = 80

largura_principal = 80
altura_principal = 80

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