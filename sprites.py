import pygame
import random
from config import largura, altura, largura_inimigo1,altura_inimigo1,largura_inimigo2,altura_inimigo2,largura_inimigo3,altura_inimigo3,largura_inimigo4,altura_inimigo4,largura_inimigo5,altura_inimigo5,largura_principal,altura_principal
from assets import IMG_TIRO_PRINCIPAL,IMG_ENEMY1,IMG_ENEMY2,IMG_ENEMY3,IMG_ENEMY4,IMG_ENEMY5,IMG_PRINCIPAL


posicoes_para_inimigosx = [0,600]

# Define a aceleração da gravidade
GRAVITY = 2
# Define a velocidade inicial no pulo
JUMP_SIZE = 20
# Define a altura do chão
GROUND = 600

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2

class Principal(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.state = STILL
        self.image = assets[IMG_PRINCIPAL]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx =  largura/2
        self.rect.bottom = 600
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        self.direcx = 0
        self.direcy = 0
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
        if self.speedx != 0:
            if self.speedx>0:
                self.direcx = 1
                self.image = self.assets[IMG_PRINCIPAL]
            else:
                self.direcx = -1
                self.image = pygame.transform.flip(self.assets[IMG_PRINCIPAL],True,False)
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            # Reposiciona para a posição do chão
            self.rect.bottom = GROUND
            # Para de cair
            self.speedy = 0
            # Atualiza o estado para parado
            self.state = STILL

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING


    def shoot(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            #A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet = Tiro_Principal(self.assets, self)
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_tiros'].add(new_bullet)

class Tiro_Principal(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[IMG_TIRO_PRINCIPAL]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.principal = principal
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = principal.rect.centerx
        self.rect.centery = principal.rect.centery
        self.speedx = 15 * principal.direcx  # Velocidade fixa para cima
        if self.speedx<0:
            self.image = pygame.transform.flip(assets[IMG_TIRO_PRINCIPAL],True,False)


    def update(self):
        # A bala só se move no eixo y
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.x < 0 or self.rect.x > 600:
            self.kill()


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
        self.shoot_ticks = 2000

    def update(self):
        # Atualização da posição da nave
        if self.principal.rect.centerx > self.rect.centerx:
            self.speedx = 3
            self.image = self.assets[IMG_ENEMY1]
        else:
            self.speedx = -3
            self.image = pygame.transform.flip(self.assets[IMG_ENEMY1],True,False)

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


class Inimigo2(pygame.sprite.Sprite):
    def __init__(self, groups, assets,principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[IMG_ENEMY2]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = 600
        self.speedx = 0
        self.groups = groups
        self.assets = assets

        self.principal = principal
        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 600

    def update(self):
        # Atualização da posição da nave
        if self.principal.rect.x >= self.rect.centerx:
            self.speedx = 3
            self.image = self.assets[IMG_ENEMY2]

        else:
            self.speedx = -3
            self.image = pygame.transform.flip(self.assets[IMG_ENEMY2],True,False)


        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

class Inimigo3(pygame.sprite.Sprite):
    def __init__(self, groups, assets,principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[IMG_ENEMY3]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 600
        self.rect.bottom = 600
        self.speedx = 0
        self.groups = groups
        self.assets = assets

        self.principal = principal
        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 2000

    def update(self):
        # Atualização da posição da nave
        if self.principal.rect.centerx > self.rect.centerx:
            self.speedx = 3
            self.image = self.assets[IMG_ENEMY3]

        else:
            self.speedx = -3
            self.image = pygame.transform.flip(self.assets[IMG_ENEMY3],True,False)


        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

class Inimigo4(pygame.sprite.Sprite):
    def __init__(self, groups, assets,principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[IMG_ENEMY4]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = 600
        self.speedx = 0
        self.groups = groups
        self.assets = assets

        self.principal = principal
        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 2000

    def update(self):
        # Atualização da posição da nave
        if self.principal.rect.centerx > self.rect.centerx:
            self.speedx = 1.5
            self.image = self.assets[IMG_ENEMY4]

        else:
            self.speedx = -1.5
            self.image = pygame.transform.flip(self.assets[IMG_ENEMY4],True,False)


        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0


class Inimigo5(pygame.sprite.Sprite):
    def __init__(self, groups, assets,principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[IMG_ENEMY5]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = 600
        self.speedx = 0
        self.groups = groups
        self.assets = assets

        self.principal = principal
        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 2000

    def update(self):
        # Atualização da posição da nave
        if self.principal.rect.centerx > self.rect.centerx:
            self.speedx = 3
            self.image = self.assets[IMG_ENEMY5]

        else:
            self.speedx = -3
            self.image = pygame.transform.flip(self.assets[IMG_ENEMY5],True,False)


        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0