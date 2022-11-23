import pygame
import os
from config import IMG, largura_inimigo1,altura_inimigo1,largura_inimigo2,altura_inimigo2,largura_inimigo3,altura_inimigo3,largura_inimigo4,altura_inimigo4,largura_inimigo5,altura_inimigo5,largura_principal,altura_principal

IMG_ENEMY1 = 'img_enemy1'
IMG_ENEMY2 = 'img_enemy2'
IMG_ENEMY3 = 'img_enemy3'
IMG_ENEMY4 = 'img_enemy4'
IMG_ENEMY5 = 'img_enemy5'
IMG_PRINCIPAL = 'img_principal'
IMG_TIRO_PRINCIPAL = 'img_tiro_principal'
IMG_TIRO_INIMIGO = 'img_tiro_inimigo'


def load_image(filename):
    return pygame.image.load(os.path.join(IMG, *filename))

def convert_alpha_image(*filename):
    return load_image(filename).convert_alpha()


def load_assets():
    assets = {}
    assets['img_enemy1'] = convert_alpha_image('Enemy01','fly01.png')
    assets['img_enemy1'] = pygame.transform.scale(assets['img_enemy1'],(largura_inimigo1,altura_inimigo1))
    assets['img_enemy2'] = convert_alpha_image('Enemy02','idle01.png')
    assets['img_enemy2'] = pygame.transform.scale(assets['img_enemy2'],(largura_inimigo2,altura_inimigo2))
    assets['img_enemy3'] = convert_alpha_image('Enemy03','idle01.png')
    assets['img_enemy3'] = pygame.transform.scale(assets['img_enemy3'],(largura_inimigo3,altura_inimigo3))
    assets['img_enemy4'] = convert_alpha_image('Enemy04','idle01.png')
    assets['img_enemy4'] = pygame.transform.scale(assets['img_enemy4'],(largura_inimigo4,altura_inimigo4))
    assets['img_enemy5'] = convert_alpha_image('Enemy05','idle01.png')
    assets['img_enemy5'] = pygame.transform.scale(assets['img_enemy5'],(largura_inimigo5,altura_inimigo5))
    assets['img_principal'] = convert_alpha_image('principal','PNG','Idle, run, jump', 'idle01.png')
    assets['img_principal'] = pygame.transform.scale(assets['img_principal'], (largura_principal, altura_principal))
    assets['img_tiro_principal'] = convert_alpha_image('principal','PNG','Throw attack', 'throw_dagger.png')
    assets['img_tiro_principal'] = pygame.transform.scale(assets['img_tiro_principal'], (40,40))
    assets['img_tiro_inimigo'] = convert_alpha_image('Enemy01','attack03.png')
    assets['img_tiro_inimigo'] = pygame.transform.scale(assets['img_tiro_inimigo'],(30,30))
    return assets