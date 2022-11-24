import pygame
from assets import load_assets
from sprites import Principal, Inimigo1, Inimigo2, Inimigo3, Inimigo4, Inimigo5
import random
pygame.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
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
groups = {}
groups['all_sprites'] = all_sprites
groups['all_meteors'] = all_inimigos
groups['all_tiros'] = all_tiros
groups['all_tiros_inimigos'] = all_tiros_inimigos
groups['all_personagens'] = all_personagens
keys_down = {}
# Criando o jogador
player = Principal(groups, assets)
all_sprites.add(player)
all_personagens.add(player)
inimigo1 = Inimigo1(groups,assets,player)
all_sprites.add(inimigo1)
all_inimigos.add(inimigo1)

inimigo2 = Inimigo2(groups,assets,player)
all_sprites.add(inimigo2)
all_inimigos.add(inimigo2)


inimigo3 = Inimigo3(groups,assets,player)
all_sprites.add(inimigo3)
all_inimigos.add(inimigo3)

inimigo4 = Inimigo4(groups,assets,player)
all_sprites.add(inimigo4)
all_inimigos.add(inimigo4)

inimigo5 = Inimigo5(groups,assets,player)
all_sprites.add(inimigo5)
all_inimigos.add(inimigo5)

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
                player.shoot()
            if event.key == pygame.K_UP:
                player.jump()
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key in keys_down and keys_down[event.key]:
                if event.key == pygame.K_LEFT:
                    player.speedx += 10
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 10
    # ----- Atualiza estado do jogo
    hits = pygame.sprite.groupcollide(all_inimigos, all_tiros, False, True, pygame.sprite.collide_mask)
    for inimigo in hits:
        inimigo.lifes -=1
        if inimigo.lifes == 0:
            inimigo.kill()


    if  int(pygame.time.get_ticks()) % 100 == 0:
        i = random.randint(1,5)
        if i == 1:
            inimigo1 = Inimigo1(groups,assets,player)
            all_sprites.add(inimigo1)
            all_inimigos.add(inimigo1)
        elif i ==2:
            inimigo2 = Inimigo2(groups,assets,player)
            all_sprites.add(inimigo2)
            all_inimigos.add(inimigo2)
        elif i == 3:
            inimigo3 = Inimigo3(groups,assets,player)
            all_sprites.add(inimigo3)
            all_inimigos.add(inimigo3)
        elif i ==4:
            inimigo4 = Inimigo4(groups,assets,player)
            all_sprites.add(inimigo4)
            all_inimigos.add(inimigo4)
        elif i ==5:
            inimigo5 = Inimigo5(groups,assets,player)
            all_sprites.add(inimigo5)
            all_inimigos.add(inimigo5)
    all_personagens.add(all_inimigos)
    all_sprites.update()
    window.fill((0,0,0))
    all_sprites.draw(window)
    for sprite in all_personagens:
        window.blit(sprite.text_surface, sprite.text_rect)
    # ----- Gera saídas
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
