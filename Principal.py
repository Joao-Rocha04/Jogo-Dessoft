#importando bibliotecas
import pygame
from assets import load_assets,ANIM_ATAQUE_PRINCIPAL,ULT
from sprites import Principal, Inimigo1, Inimigo2, Inimigo3, Inimigo4, Inimigo5
import random
#inicio do jogo
pygame.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
now1 = 0
pygame.display.set_caption('Hello World!')
# ----- Inicia estruturas de dados
game = True
assets = load_assets()
# ----- Inicia assets
# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
all_inimigos = pygame.sprite.Group()
all_tiros = pygame.sprite.Group()
all_tiros_inimigos = pygame.sprite.Group()
all_personagens = pygame.sprite.Group()
all_tiros_especial = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_inimigos'] = all_inimigos
groups['all_tiros'] = all_tiros
groups['all_tiros_inimigos'] = all_tiros_inimigos
groups['all_personagens'] = all_personagens
groups['all_tiros_especial'] = all_tiros_especial
keys_down = {}
print(pygame.font.get_fonts())
# Criando o jogador
player = Principal(groups, assets) 
all_sprites.add(player)
all_personagens.add(player)
score = 0
ult = 0
last_hit = 0
last_hit1 = 0
font = pygame.font.SysFont(None, 48)
# ===== Loop principal =====
while game:
    clock.tick(30)
    # ----- Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            keys_down[event.key] = True
            if event.key == pygame.K_LEFT:
                player.speedx -= 10
                ultima_tecla = True
            if event.key == pygame.K_RIGHT:
                player.speedx += 10
                ultima_tecla = False
            if event.key == pygame.K_SPACE:
                player.ataque = True
                player.shoot()
            if event.key == pygame.K_UP:
                player.jump()
            if event.key == pygame.K_q:
                if ult==100:
                    player.especial1 = True
                    ult = 0
            if event.key == pygame.K_e:
                if player.direita == True:
                    player.rect.centerx = player.rect.centerx + 100
                else:
                    player.rect.centerx = player.rect.centerx - 100
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key in keys_down and keys_down[event.key]:
                if event.key == pygame.K_LEFT:
                    player.speedx += 10
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 10
    # ----- Atualiza estado do jogo
    if ult!= 100:
        text = font.render(f'ESPECIAL = {ult}%', True, (0, 0, 0))
    if ult == 100:
        text = font.render(f'ESPECIAL PRONTO (Q)', True, (0, 0, 0))
    pontos = font.render(f'Pontos = {score}', True, (0, 0, 0))
    hits1 = pygame.sprite.groupcollide(all_inimigos, all_tiros_especial, True, False, pygame.sprite.collide_mask)
    hits = pygame.sprite.groupcollide(all_inimigos, all_tiros, False, True, pygame.sprite.collide_mask)
    for inimigo in hits:
        inimigo.hit = True
        inimigo.lifes -=1
        if inimigo.lifes == 0:
            inimigo.kill()
            if ult!= 100:
                ult += 5
            score += 100
    hit_principal = pygame.sprite.spritecollide(player,all_tiros_inimigos,True)
    if len(hit_principal)>0:
        if player.sprite != player.assets[ANIM_ATAQUE_PRINCIPAL]:
            player.lifes = player.lifes - len(hit_principal)
            player.atual = 0
            player.hit = True
            if player.lifes <= 0:
                player.atual = 0
                #player.morte = True
                player.kill()
                game = False 
    now = pygame.time.get_ticks()
    hit_ticks = 1500
    hit_principal1 = pygame.sprite.spritecollide(player,all_inimigos,False)
    if now - last_hit> hit_ticks:
        last_hit = now
        if len(hit_principal1)>0:
            if player.sprite != player.assets[ANIM_ATAQUE_PRINCIPAL]:
                player.lifes = player.lifes - 1
                player.atual = 0
                player.hit = True
                if player.lifes <= 0:
                    #player.morte= True
                    player.kill()
                    game = False
    now1 = pygame.time.get_ticks()
    hit_ticks1 = 2000
    if now1 - last_hit1> hit_ticks1:
        hit_ticks1-=20
        last_hit1 = now1
        i = random.randint(1,5)
        if i == 1:
            inimigo = Inimigo1(groups,assets,player)
            all_sprites.add(inimigo)
            all_inimigos.add(inimigo)
        elif i ==2:
            inimigo = Inimigo2(groups,assets,player)
            all_sprites.add(inimigo)
            all_inimigos.add(inimigo)
        elif i == 3:
            inimigo = Inimigo3(groups,assets,player)
            all_sprites.add(inimigo)
            all_inimigos.add(inimigo)
        elif i ==4:
            inimigo = Inimigo4(groups,assets,player)
            all_sprites.add(inimigo)
            all_inimigos.add(inimigo)
        elif i ==5:
            inimigo = Inimigo5(groups,assets,player)
            all_sprites.add(inimigo)
            all_inimigos.add(inimigo)
    all_personagens.add(all_inimigos)
    all_sprites.update()
    window.fill((0,0,0))
    window.blit(assets['background3'], (0, 0))
    window.blit(text, (10, 10))
    window.blit(pontos, (750, 10))
    all_sprites.draw(window)
    for sprite in all_personagens:
        window.blit(sprite.text_surface, sprite.text_rect)
    # ----- Gera saídas
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
