#importando bibliotecas
import pygame
import random
from config import largura
from assets import ATAQUE_INI3,IMG_TIRO_PRINCIPAL1,ATAQUE_INI4,MORTE,HIT_PRINCIPAL,ATTACK_INIMIGO2,ANIM_ATAQUE_INI5,ANIM_ATAQUE_PRINCIPAL,ANIM_TIRO,WALK_PRINCIPAL,WALK_INIMIGO5,WALK_INIMIGO4,WALK_INIMIGO3,WALK_INIMIGO2,HIT_INIMIGO1,VOO_INIMIGO1,SCORE_FONT,IMG_TIRO_INIMIGO,IMG_TIRO_PRINCIPAL,IMG_ENEMY1,IMG_ENEMY2,IMG_ENEMY3,IMG_ENEMY4,IMG_ENEMY5,IMG_PRINCIPAL
import math

posicoes_para_inimigosx = [0,1000]

# Define a aceleração da gravidade
GRAVITY = 2
# Define a velocidade inicial no pulo
JUMP_SIZE = 25
# Define a altura do chão
GROUND = 600

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2

#classe do personagem principal
class Principal(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.state = STILL
        self.sprite = assets[WALK_PRINCIPAL]
        self.atual = 0
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
        self.shoot_ticks = 500
        self.lifes = 3
        self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
        self.direita = True
        self.ataque = False
        self.hit = False
        self.morte = False
        self.contador = 0
        self.especial1 = False
    #update do principal personagem
    def update(self):
        #animação do especial
        if self.especial1 == True:
            self.sprite = self.assets[ANIM_ATAQUE_PRINCIPAL]
            if self.atual>len(self.sprite):
                if self.contador == 1:
                    self.especial()
                    self.especial1 = False
                    self.sprite = self.assets[WALK_PRINCIPAL]
                    self.contador = 0
                self.contador+=1
                self.atual = 0
            if self.direita == True:
                self.image = self.sprite[int(self.atual)]
            else:
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)
            self.atual+=0.3
        #animação do hit do personagem
        elif self.hit == True:
            self.sprite = self.assets[HIT_PRINCIPAL]
            if self.atual>= len(self.sprite):
                self.sprite = self.assets[WALK_PRINCIPAL]
                self.hit = False
            if self.direita == True:
                self.image = self.sprite[int(self.atual)]
            else:
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)
            self.atual+=0.1
        elif self.ataque == True:
            self.sprite = self.assets[ANIM_TIRO]
            if self.atual>= len(self.sprite):
                self.sprite = self.assets[WALK_PRINCIPAL]
                self.shoot()
                self.ataque = False
            if self.direita == True:
                self.image = self.sprite[int(self.atual)]
            else:
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)
            self.atual+=0.6
        #animação de andar
        else:
            self.sprite = self.assets[WALK_PRINCIPAL]
            # Atualização da posição da nave
            self.atual= self.atual + 0.3
            if self.atual>= len(self.sprite): 
                self.atual = 0
            # Mantem dentro da tela
            if self.rect.right > largura:
                self.rect.right = largura
            if self.rect.left < 0:
                self.rect.left = 0
            if self.speedx != 0:
                if self.speedx>0:
                    self.direcx = 1
                    self.image = self.sprite[int(self.atual)]
                    self.direita = True
                else:
                    self.direcx = -1
                    self.image = self.sprite[int(self.atual)]
                    self.image = pygame.transform.flip(self.image,True,False)
                    self.direita = False
            else:
                self.image = self.assets[IMG_PRINCIPAL]
                if self.direita== True:
                    self.image = self.assets[IMG_PRINCIPAL]
                else:
                    self.image = pygame.transform.flip(self.image,True,False)
            
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
            self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
            self.text_rect = self.text_surface.get_rect()
            self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
            self.rect.x += self.speedx
        # Método que faz o personagem pular
    def jump(self):
            # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING


    #função para o personagem atirar
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
    #função para o ataque especial do personagem
    def especial(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot
        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            #A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet = Tiro_Especial(self.assets, self)
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_tiros_especial'].add(new_bullet)
#classe pro tiro primário do personagem
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
        self.rect.centery = principal.rect.centery+20
        self.speedx = 15 * principal.direcx  # Velocidade fixa para cima
        if self.speedx<0:
            self.image = pygame.transform.flip(assets[IMG_TIRO_PRINCIPAL],True,False)
    def update(self):
        # A bala só se move no eixo x
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.x < 0 or self.rect.x > largura:
            self.kill()

#classe para o especial do principal
class Tiro_Especial(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[IMG_TIRO_PRINCIPAL1]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.principal = principal
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = principal.rect.centerx
        self.rect.centery = principal.rect.centery+20
        self.speedx = 15 * principal.direcx  # Velocidade fixa para cima
        if self.speedx<0:
            self.image = pygame.transform.flip(assets[IMG_TIRO_PRINCIPAL1],True,False)
    def update(self):
        # A bala só se move no eixo x
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.x < 0 or self.rect.x > largura:
            self.kill()

#classe para o primeiro inimigo
class Inimigo1(pygame.sprite.Sprite):
    def __init__(self, groups, assets,principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.hit = False
        self.atual = 0
        self.sprite = assets[VOO_INIMIGO1]
        self.spritehit1 = assets[HIT_INIMIGO1]
        self.image = self.sprite[self.atual]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = 500
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        self.lifes = 1
        self.principal = principal
        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 2000
        self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
        self.direita = True
    def update(self):
        #caso o inimigo sofra hit
        if self.hit == True:
            self.sprite = self.assets[HIT_INIMIGO1]
            if self.atual>= len(self.sprite):
                self.sprite = self.assets[VOO_INIMIGO1]
                self.hit = False
            if self.direita == True:
                self.image = self.sprite[int(self.atual)]
            else:
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)
            self.atual+=0.3
        #quando o inimigo estiver voando
        else:
            if self.atual>= len(self.sprite): 
                self.atual = 0
            self.image = self.sprite[int(self.atual)]

            if self.principal.rect.centerx > self.rect.centerx:
                self.direita = True
                self.image = self.sprite[int(self.atual)]
                self.speedx = 3
            else:
                self.direita = False
                self.speedx = -3
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)



            # Mantem dentro da tela
            if self.rect.right > largura:
                self.rect.right = largura
            if self.rect.left < 0:
                self.rect.left = 0
            now = pygame.time.get_ticks()
            # Verifica quantos ticks se passaram desde o último tiro.
            elapsed_ticks = now - self.last_shot

            # Se já pode atirar novamente...
            if elapsed_ticks > self.shoot_ticks:
                self.shoot()

            #mostra as vidas do inimigo
            self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
            self.text_rect = self.text_surface.get_rect()
            self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
            self.atual= self.atual + 0.3
    #tiro do inimigo
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
            novo_tiro_inimigo = Tiro_inimigo(self.assets, self.principal,self,self.groups)
            self.groups['all_sprites'].add(novo_tiro_inimigo)
            self.groups['all_tiros_inimigos'].add(novo_tiro_inimigo)

#classe para o tiro do inimigo
class Tiro_inimigo(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, principal,inimigo,groups):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.x = principal.rect.centerx
        self.y = principal.rect.centery
        self.image = assets[IMG_TIRO_INIMIGO]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.principal = principal
        self.inimigo = inimigo
        self.rect.x = self.inimigo.rect.x
        self.rect.y = self.inimigo.rect.y
        # Coloca no lugar inicial definido em x, y do constutor
        self.ball_speed_x = 0
        self.ball_speed_y = 0
        #Posição inicial da bola
        self.ball_x = inimigo.rect.x
        self.ball_y = inimigo.rect.y
        self.ACELERACAO = .5
        self.groups = groups
        #faz a conta para onde o tiro tem que ir
        self.angulo = math.atan((self.ball_y - self.y) / (self.ball_x - self.x))
    #faz o update do tiro
    def update(self):
        forca = 17
        ball_speed_x = math.cos(self.angulo) * forca
        ball_speed_y = math.sin(self.angulo) * forca
        self.rect.centerx += ball_speed_x
        self.rect.centery += ball_speed_y
        if self.rect.x > 1000 or self.rect.x<0 or self.rect.y>1000 or self.rect.y<0:
            self.kill()




#define classe do inimigo 2
class Inimigo2(pygame.sprite.Sprite):
    def __init__(self, groups, assets,principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.atual = 0
        self.sprite = assets[WALK_INIMIGO2]
        self.image = self.sprite[self.atual]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(posicoes_para_inimigosx)
        self.rect.bottom = 600
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        self.lifes = 1
        self.principal = principal
        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 600
        self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
        self.ataque = False
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 1000
        self.direita = True
    #update da posição do inimigo
    def update(self):
        x = True
        # Animação para o ataque do inimigo 2
        if self.ataque == True:
            self.sprite = self.assets[ATTACK_INIMIGO2]
            if self.atual> 8:
                self.atual = 0
            if self.atual>= len(self.sprite)+0.1:
                self.ataque = False
                x = False
                self.sprite = self.assets[WALK_INIMIGO2]
            if x == True:
                if self.direita == True:
                    self.image = self.sprite[int(self.atual)]
                else:
                    self.image = self.sprite[int(self.atual)]
                    self.image = pygame.transform.flip(self.image,True,False)
            self.atual+=0.3
        #animação de andar do inimigo 2
        else:
            self.sprite = self.assets[WALK_INIMIGO2]
            if self.atual>= len(self.sprite): 
                self.atual = 0
            self.image = self.sprite[int(self.atual)]
            if self.principal.rect.centerx > self.rect.centerx:
                self.direita = True
                self.speedx = 5
                self.image = self.sprite[int(self.atual)]
            else:
                self.direita = False
                self.speedx = -5
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)

            self.rect.x += self.speedx
            self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
            self.text_rect = self.text_surface.get_rect()
            self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
            # Mantem dentro da tela
            if self.rect.right > largura:
                self.rect.right = largura
            if self.rect.left < 0:
                self.rect.left = 0
            aaa = self.principal.rect.centerx - self.rect.centerx
            now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
            elapsed_ticks = now - self.last_shot
            # Se já pode atirar novamente...
            if elapsed_ticks > self.shoot_ticks and -40 <= aaa <=40:
            # Marca o tick da nova imagem.
                self.last_shot = now
                self.ataque = True
            self.atual= self.atual + 0.3
#classe para o inimigo 3
class Inimigo3(pygame.sprite.Sprite):
    def __init__(self, groups, assets,principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.atual = 0
        self.sprite = assets[WALK_INIMIGO3]
        self.image = self.sprite[self.atual]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(posicoes_para_inimigosx)
        self.rect.bottom = 600
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        self.lifes = 2
        self.principal = principal
        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 2000
        self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
        self.direita = True
        self.atual = 0
        self.ataque = False
        self.contador = 0
    #faz o update da posição do inimigo 3
    def update(self):
        #ataque do inimigo 3
        if self.ataque == True:
            self.sprite = self.assets[ATAQUE_INI3]
            if self.atual>len(self.sprite):
                if self.contador == 1:
                    self.ataque = False
                    self.sprite = self.assets[WALK_INIMIGO3]
                    self.contador = 0
                self.contador+=1
                self.atual = 0
            if self.direita == False:
                self.image = self.sprite[int(self.atual)]
            else:
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)
            self.atual+=0.3
        #andar do inimigo 3
        else:
        # Atualização da posição da nave
            self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
            self.text_rect = self.text_surface.get_rect()
            self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
            self.atual= self.atual + 0.3
            if self.atual>= len(self.sprite): 
                self.atual = 0
            self.image = self.sprite[int(self.atual)]
            if self.principal.rect.centerx > self.rect.centerx:
                self.direita = True
                self.speedx = 2
                self.image = self.sprite[int(self.atual)]

            else:
                self.direita = False
                self.speedx = -2
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)
            self.rect.x += self.speedx
            aaa = self.principal.rect.centerx - self.rect.centerx
            now = pygame.time.get_ticks()
            # Verifica quantos ticks se passaram desde o último tiro.
            elapsed_ticks = now - self.last_shot
                # Se já pode atirar novamente...
            if elapsed_ticks > self.shoot_ticks and -40 <= aaa <=40:
                # Marca o tick da nova imagem.
                self.last_shot = now
                self.ataque = True
            self.atual= self.atual + 0.3

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

#classe para o inimigo 4
class Inimigo4(pygame.sprite.Sprite):
    def __init__(self, groups, assets,principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.atual = 0
        self.sprite = assets[WALK_INIMIGO4]
        self.image = self.sprite[self.atual]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(posicoes_para_inimigosx)
        self.rect.bottom = 600
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        self.lifes = 2
        self.principal = principal
        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
        self.ataque = False
        self.direita = True
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 1000
        self.contador = 0
    #faz o update do inimigo 4
    def update(self):
        #ataque do inimigo 4
        if self.ataque == True:
            self.sprite = self.assets[ATAQUE_INI4]
            if self.atual>len(self.sprite):
                if self.contador == 1:
                    self.ataque = False
                    self.sprite = self.assets[WALK_INIMIGO4]
                    self.contador = 0
                self.contador+=1
                self.atual = 0
            if self.direita == True:
                self.image = self.sprite[int(self.atual)]
            else:
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)
            self.atual+=0.3
        #andar o inimigo 4
        else:
            if self.atual>= len(self.sprite): 
                self.atual = 0
            self.image = self.sprite[int(self.atual)]
            if self.principal.rect.centerx > self.rect.centerx:
                self.direita = True
                self.speedx = 2
                self.image = self.sprite[int(self.atual)]
            else:
                self.direita = False
                self.speedx = -2
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)
            self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
            self.text_rect = self.text_surface.get_rect()
            self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
            self.rect.x += self.speedx
            # Mantem dentro da tela
            if self.rect.right > largura:
                self.rect.right = largura
            if self.rect.left < 0:
                self.rect.left = 0
            aaa = self.principal.rect.centerx - self.rect.centerx
            now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
            elapsed_ticks = now - self.last_shot
            # Se já pode atirar novamente...
            if elapsed_ticks > self.shoot_ticks and -30 <= aaa <=30:
            # Marca o tick da nova imagem.
                self.last_shot = now
                self.ataque = True
            self.atual= self.atual + 0.3
#classe do inimigo 5
class Inimigo5(pygame.sprite.Sprite):
    def __init__(self, groups, assets,principal):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.atual = 0
        self.sprite = assets[WALK_INIMIGO5]
        self.image = self.sprite[self.atual]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(posicoes_para_inimigosx)
        self.rect.bottom = 600
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        self.lifes = 3
        self.principal = principal
        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 2000
        self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
        self.direita = True
        self.ataque = False
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 1000
    #faz o update do inimigo 5
    def update(self):
        # Atualização da posição da nave
        #ataque do inimigo 5
        if self.ataque == True:
            self.sprite = self.assets[ANIM_ATAQUE_INI5]
            if self.atual>len(self.sprite)+0.1:
                self.atual = 0
            if self.atual>= len(self.sprite):
                self.ataque = False
                self.sprite = self.assets[WALK_INIMIGO5]
            if self.direita == True:
                self.image = self.sprite[int(self.atual)]
            else:
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)
            self.atual+=0.3
        #andar do inimigo 5
        else:
            self.sprite = self.assets[WALK_INIMIGO5]
            if self.atual>= len(self.sprite): 
                self.atual = 0
            self.image = self.sprite[int(self.atual)]
            if self.principal.rect.centerx > self.rect.centerx:
                self.direita = True
                self.speedx = 3
                self.image = self.sprite[int(self.atual)]
            else:
                self.direita = False
                self.speedx = -3
                self.image = self.sprite[int(self.atual)]
                self.image = pygame.transform.flip(self.image,True,False)
            self.rect.x += self.speedx
            self.text_surface = self.assets[SCORE_FONT].render(chr(9829) * self.lifes, True, (255,0,0))
            self.text_rect = self.text_surface.get_rect()
            self.text_rect.bottomleft = (self.rect.x-5,self.rect.top+10)
            # Mantem dentro da tela
            if self.rect.right > largura:
                self.rect.right = largura
            if self.rect.left < 0:
                self.rect.left = 0
            aaa = self.principal.rect.centerx - self.rect.centerx
            now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
            elapsed_ticks = now - self.last_shot
            # Se já pode atirar novamente...
            if elapsed_ticks > self.shoot_ticks and -30 <= aaa <=30:
            # Marca o tick da nova imagem.
                self.last_shot = now
                self.ataque = True
            self.atual= self.atual + 0.3