import pygame
from assets import load_assets
from sprites import Principal, Inimigo1, Inimigo2
pygame.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')
# ----- Inicia estruturas de dados
game = True
assets = load_assets()
# ----- Inicia assets
image = assets['img_enemy1']
# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
all_meteors = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_meteors'] = all_meteors
groups['all_bullets'] = all_bullets
keys_down = {}
# Criando o jogador
player = Principal(groups, assets)
all_sprites.add(player)
inimigo1 = Inimigo1(groups,assets,player)
all_sprites.add(inimigo1)
inimigo2 = Inimigo2(groups,assets,player)
all_sprites.add(inimigo2)
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
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key in keys_down and keys_down[event.key]:
                if event.key == pygame.K_LEFT:
                    player.speedx += 10
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 10
    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()
    window.fill((0,0,0))
    all_sprites.draw(window)
    # ----- Gera saídas
    window.blit(image, (10, 10))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
