import pygame

helicopter_1 = pygame.image.load('sprites/helicopter_1.png')
jet_1 = pygame.image.load('sprites/jet_1.png')
helicopter_2 = pygame.image.load('sprites/helicopter_2.png')
explosion_0 = pygame.image.load('sprites/explosion_0.png')
explosion_1 = pygame.image.load('sprites/explosion_1.png')
explosion_2 = pygame.image.load('sprites/explosion_2.png')
explosion_3 = pygame.image.load('sprites/explosion_3.png')
explosion_4 = pygame.image.load('sprites/explosion_4.png')
explosion_5 = pygame.image.load('sprites/explosion_5.png')
explosion_6 = pygame.image.load('sprites/explosion_6.png')
explosion_7 = pygame.image.load('sprites/explosion_7.png')
helicopter_damaged_1 = pygame.image.load('sprites/helicopter_damaged_1.png')
helicopter_damaged_2 = pygame.image.load('sprites/helicopter_damaged_2.png')
enemy_helicopter_1 = pygame.image.load('sprites/enemy_helicopter_1.png')
enemy_helicopter_2 = pygame.image.load('sprites/enemy_helicopter_2.png')
boat = pygame.image.load('sprites/boat.png')

helicopter_list = [jet_1, helicopter_2]
damage_helicopter_list = [helicopter_damaged_1, helicopter_damaged_2]
enemy_helicopter_list = [enemy_helicopter_1, enemy_helicopter_2]
balloon = pygame.image.load('sprites/balloon.png')
spaceship = pygame.image.load('sprites/balloon.png')
icon = pygame.image.load('sprites/icon.png')
background = pygame.image.load('sprites/background.png')
cloud = pygame.image.load('sprites/cloud.png')

all_sprites = [jet_1, helicopter_2, helicopter_damaged_1, helicopter_damaged_2, enemy_helicopter_1,
               enemy_helicopter_2, explosion_0, explosion_1, explosion_2, explosion_3, explosion_4, explosion_5,
               explosion_6, explosion_7, boat, balloon, spaceship, icon, background, cloud]
