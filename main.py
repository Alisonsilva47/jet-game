import pygame
import jet
import enemy
import boat
import sprites
import random

font = "8-Bit-Madness.ttf"

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

pygame.display.set_icon(sprites.icon)
display_width = 800
display_height = 600
game.display = pygame.display.set_mode((display_width, display_height))


def message_to_screen(message, textfont, size, color):
    my_font = pygame.font.Font(textfont, size)
    my_message = my_font.render(message, 0, color)
    return my_message


white, black, gray = ((255, 255, 255), (0, 0, 0), (50, 50, 50))
red, green, blue, yellow = ((255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0))


for convert_sprites in sprites.all_sprites:
    convert_sprites.convert_alpha()

clock = pygame.time.clock()
fps = 30

player = jet.Jet = open(100, display_height/2-40)
moving = True
godmode = False

score = 0
high_score_file = open('highscore.dat', 'r')
high_score_init = int(high_score_file.read())

cloud_x = 800
cloud_y = random.randint(0, 400)

enemy = enemy.Enemy(-100, display_height/2-40)
enemy_alive = False
boat = boat.Boat(-110, 430)
boat_alive = False

spaceship_x = 800
spaceship_y = random.randint(0, 400)
spaceship_alive = False
spaceship_hit_player = False
warning_once = True
warning = False
warning_counter = 0
warning_message = message_to_screen("!", font, 200, red)


balloon_x = 800
balloon_y = random.randint(0, 400)

 
