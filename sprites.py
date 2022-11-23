import pygame
import random
from config import largura, altura, largura_inimigo1,altura_inimigo1,largura_inimigo2,altura_inimigo2,largura_inimigo3,altura_inimigo3,largura_inimigo4,altura_inimigo4,largura_inimigo5,altura_inimigo5,largura_principal,altura_principal
from assets import IMG_ENEMY1,IMG_ENEMY2,IMG_ENEMY3,IMG_ENEMY4,IMG_ENEMY5,IMG_PRINCIPAL


posicoes_para_inimigosx = [0,600]


class Principal(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[IMG_PRINCIPAL]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx =  largura/2
        self.rect.bottom = 600
        self.speedx = 0
        self.groups = groups
        self.assets = assets

        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 1000

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            #new_bullet = Bullet(self.assets, self.rect.top, self.rect.centerx)
            #self.groups['all_sprites'].add(new_bullet)
            #self.groups['all_bullets'].add(new_bullet)



class Inimigo1(pygame.sprite.Sprite):
    def __init__(self, groups, assets,principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[IMG_ENEMY1]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = 500
        self.speedx = 0
        self.groups = groups
        self.assets = assets

        self.principal = principal
        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500

    def update(self):
        # Atualização da posição da nave
        if self.principal.rect.x > self.rect.x:
            self.speedx = 5
        else:
            self.speedx = -5

        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            #new_bullet = Bullet(self.assets, self.rect.top, self.rect.centerx)
            #self.groups['all_sprites'].add(new_bullet)
            #self.groups['all_bullets'].add(new_bullet)
            #self.assets[PEW_SOUND].play()