#immportando bibliotecas
import pygame
import os
from config import largura,altura,FNT,IMG, largura_inimigo1,altura_inimigo1,largura_inimigo2,altura_inimigo2,largura_inimigo3,altura_inimigo3,largura_inimigo4,altura_inimigo4,largura_inimigo5,altura_inimigo5,largura_principal,altura_principal

#itens do dicionário
IMG_ENEMY1 = 'img_enemy1'
IMG_ENEMY2 = 'img_enemy2'
IMG_ENEMY3 = 'img_enemy3'
IMG_ENEMY4 = 'img_enemy4'
IMG_ENEMY5 = 'img_enemy5'
IMG_PRINCIPAL = 'img_principal'
IMG_TIRO_PRINCIPAL = 'img_tiro_principal'
IMG_TIRO_PRINCIPAL1 = 'img_tiro_principal1'
IMG_TIRO_INIMIGO = 'img_tiro_inimigo'
SCORE_FONT = 'score_font'
BACKGROUND = 'background'
VOO_INIMIGO1 = 'voo_inimigo1'
HIT_INIMIGO1 = 'hit_inimigo1'
ATTACK_INIMIGO2 = 'attack_inimigo2'
HIT_INIMIGO2 = 'hit_inimigo2'
WALK_INIMIGO2 = 'walk_inimigo2'
WALK_INIMIGO3 = 'walk_inimigo3'
WALK_INIMIGO4 = 'walk_inimigo4'
WALK_INIMIGO5 = 'walk_inimigo5'
WALK_PRINCIPAL = 'walk_principal'
ANIM_TIRO = 'anim_tiro'
ANIM_ATAQUE_PRINCIPAL = 'anim_ataque_principal'
ANIM_ATAQUE_INI5 = 'anim_ataque_ini5'
MORTE = 'morte'
HIT_PRINCIPAL = 'hit_principal'
ATAQUE_INI4 = 'ataque_ini4'
ATAQUE_INI3 = 'ataque_ini3'
ULT = 'ult'
#funções para importar imagens e animações
def load_image(filename):
    return pygame.image.load(os.path.join(IMG, *filename))
def convert_alpha_image(*filename):
    return load_image(filename).convert_alpha()
def load_font(filename):
    return pygame.font.Font(os.path.join(FNT,*filename))

#função que vai importar todos os sprites
def load_assets():
    #criando dicionário
    assets = {}
    #importando imagens
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
    assets['img_tiro_principal1'] = convert_alpha_image('principal','PNG','Throw attack', 'throw_dagger.png')
    assets['img_tiro_principal1'] = pygame.transform.scale(assets['img_tiro_principal'], (100,150))
    assets['img_tiro_inimigo'] = convert_alpha_image('Enemy01','attack03.png')
    assets['img_tiro_inimigo'] = pygame.transform.scale(assets['img_tiro_inimigo'],(30,30))
    assets['score_font'] = pygame.font.Font(os.path.join(FNT, 'PressStart2P.ttf'), 10)
    assets['background'] = convert_alpha_image('backgrounds','12.png')
    assets['background'] = pygame.transform.scale(assets['background'],(largura,altura))
    assets['background2'] = convert_alpha_image('backgrounds','14.png')
    assets['background2'] = pygame.transform.scale(assets['background2'],(largura,altura))
    assets['background3'] = convert_alpha_image('backgrounds','40.png')
    assets['background3'] = pygame.transform.scale(assets['background3'],(largura,altura))
    #importando todas as animações

    voo_inimigo1 = []
    for i in range(1,7):
        img = convert_alpha_image('Enemy01',f'fly0{i}.png')
        img = pygame.transform.scale(img,(largura_inimigo1,altura_inimigo1))
        voo_inimigo1.append(img)
    assets[VOO_INIMIGO1] = voo_inimigo1
    hit_inimigo1 = []
    for i in range(1,3):
        img = convert_alpha_image('Enemy01',f'hit0{i}.png')
        img = pygame.transform.scale(img,(largura_inimigo1,altura_inimigo1))
        hit_inimigo1.append(img)
    assets[HIT_INIMIGO1] = hit_inimigo1
    attack_inimigo2 = []
    for i in range(1,8):
        img = convert_alpha_image('Enemy02',f'attack0{i}.png')
        img = pygame.transform.scale(img,(largura_inimigo2,altura_inimigo2))
        attack_inimigo2.append(img)
    assets[ATTACK_INIMIGO2] = attack_inimigo2
    hit_inimigo2 = []
    for i in range(1,3):
        img = convert_alpha_image('Enemy02',f'hit0{i}.png')
        img = pygame.transform.scale(img,(largura_inimigo2,altura_inimigo2))
        hit_inimigo2.append(img)
    assets[HIT_INIMIGO2] = hit_inimigo2
    walk_inimigo3 = []
    for i in range(1,8):
        img = convert_alpha_image('Enemy03',f'idle0{i}.png')
        img = pygame.transform.scale(img,(largura_inimigo3,altura_inimigo3))
        walk_inimigo3.append(img)
    assets[WALK_INIMIGO3] = walk_inimigo3
    walk_inimigo4 = []
    for i in range(1,7):
        img = convert_alpha_image('Enemy04',f'idle0{i}.png')
        img = pygame.transform.scale(img,(largura_inimigo4,altura_inimigo4))
        walk_inimigo4.append(img)
    assets[WALK_INIMIGO4] = walk_inimigo4
    walk_inimigo5 = []
    for i in range(1,9):
        img = convert_alpha_image('Enemy05',f'idle0{i}.png')
        img = pygame.transform.scale(img,(largura_inimigo5,altura_inimigo5))
        walk_inimigo5.append(img)
    assets[WALK_INIMIGO5] = walk_inimigo5
    walk_inimigo2 = []
    for i in range(1,8):
        img = convert_alpha_image('Enemy02',f'walk0{i}.png')
        img = pygame.transform.scale(img,(largura_inimigo2,altura_inimigo2))
        walk_inimigo2.append(img)
    assets[WALK_INIMIGO2] = walk_inimigo2
    walk_principal = []
    for i in range(1,8):
        img = convert_alpha_image('principal','PNG','Idle, run, jump',f'run0{i}.png')
        img = pygame.transform.scale(img,(largura_principal,altura_principal))
        walk_principal.append(img)
    assets[WALK_PRINCIPAL] = walk_principal
    anim_tiro = []
    for i in range(1,4):
        img = convert_alpha_image('principal','PNG','Throw attack',f'throw_attack0{i}.png')
        img = pygame.transform.scale(img,(largura_principal,altura_principal))
        anim_tiro.append(img)
    assets[ANIM_TIRO] = anim_tiro
    anim_ataque_principal = []
    for i in range(1,8):
        img = convert_alpha_image('principal','PNG','Attacks',f'AttackD0{i}.png')
        img = pygame.transform.scale(img,(largura_principal,altura_principal))
        anim_ataque_principal.append(img)
    assets[ANIM_ATAQUE_PRINCIPAL] = anim_ataque_principal
    ataque_ini5 = []
    for i in range(1,6):
        img = convert_alpha_image('Enemy05',f'attack0{i}.png')
        img = pygame.transform.scale(img,(largura_inimigo5,altura_inimigo5))
        ataque_ini5.append(img)
    assets[ANIM_ATAQUE_INI5] = ataque_ini5
    morte = []
    for i in range(1,5):
        img = convert_alpha_image('principal','PNG','Hit, death',f'death0{i}.png')
        img = pygame.transform.scale(img,(largura_principal,altura_principal))
        morte.append(img)
    assets[MORTE] = morte
    hit_principal = []
    for i in range(1,3):
        img = convert_alpha_image('principal','PNG','Hit, death',f'hit0{i}.png')
        img = pygame.transform.scale(img,(largura_principal,altura_principal))
        hit_principal.append(img)
    assets[HIT_PRINCIPAL] = hit_principal
    ataqueini4 = []
    for i in range(1,7):
        img = convert_alpha_image('Enemy04',f'attack0{i}.png')
        img = pygame.transform.scale(img,(largura_inimigo4,altura_inimigo4))
        ataqueini4.append(img)
    assets[ATAQUE_INI4]= ataqueini4
    ataque3 = []
    for i in range(1,8):
        img = convert_alpha_image('Enemy03',f'attack_right0{i}.png')
        img = pygame.transform.scale(img,(largura_inimigo3,altura_inimigo3))
        ataque3.append(img)
    assets[ATAQUE_INI3] = ataque3
    return assets