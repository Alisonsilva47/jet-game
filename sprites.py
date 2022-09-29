import pygame

jet_1 = pygame.image.load('sprites/jet_1.png')
explosion_0 = pygame.image.load('sprites/explosion_0.png')
explosion_1 = pygame.image.load('sprites/explosion_1.png')
explosion_2 = pygame.image.load('sprites/explosion_2.png')
explosion_3 = pygame.image.load('sprites/explosion_3.png')
explosion_4 = pygame.image.load('sprites/explosion_4.png')
explosion_5 = pygame.image.load('sprites/explosion_5.png')
explosion_6 = pygame.image.load('sprites/explosion_6.png')
explosion_7 = pygame.image.load('sprites/explosion_7.png')
jet_damaged_1 = pygame.image.load('sprites/jet_damaged.png')
jet_damaged_2 = pygame.image.load('sprites/jet_damaged.png')
enemy_jet_1 = pygame.image.load('sprites/enemy_jet_1.png')
tank = pygame.image.load('sprites/tank.png')
heart = pygame.image.load('sprites/heart.png')

jet_list = [jet_1]
damage_jet_list = [jet_damaged_1, jet_damaged_2]
enemy_jet_list = [enemy_jet_1]
atomic_bomb = pygame.image.load('sprites/atomic_bomb.png')
spaceship = pygame.image.load('sprites/atomic_bomb.png')
icon = pygame.image.load('sprites/icon.png')
background = pygame.image.load('sprites/background.png')
background_blur = pygame.image.load('sprites/background_blur.png')
# ground = pygame.image.load('sprites/ground.png')
cloud = pygame.image.load('sprites/cloud.png')

all_sprites = [jet_1, jet_damaged_1, jet_damaged_2, enemy_jet_1,
               explosion_0, explosion_1, explosion_2, explosion_3, explosion_4, explosion_5,
               explosion_6, explosion_7, atomic_bomb, spaceship, icon, background, cloud]
