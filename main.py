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
red, green, blue, yellow = (
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0))


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

bullets = []

bombs = []

pop = pygame.mixer.sound('sounds/pop.wav')
bomb = pygame.mixer.sound('sounds/bomb.wav')
explosion = pygame.mixer.sound('sounds/explosion.wav')
explosion2 = pygame.mixer.sound('sounds/explosion2.wav')
select = pygame.mixer.sound('sounds/select.wav')
select2 = pygame.mixer.sound('sounds/select2.wav')
alert = pygame.mixer.sound('sounds/alert.wav')
whoosh = pygame.mixer.sound('sounds/whoosh.wav')


def main_menu():
    global cloud_x
    global cloud_y

    menu = True

    selected = "play"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_W or event.key == pygame.K_UP:
                    pygame.mixer.Sound.play(select)
                    selected = "play"

                elif event.key == pygame.K_S or event.key == pygame.K_DOWN:
                    pygame.mixer.Sound.play(select)
                    selected = "quit"

                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    pygame.mixer.Sound.play(select2)
                    if (selected == "play"):
                        menu = False
                    if select == "quit":
                        pygame.quit()
                        quit()

        game_display.blit(sprites.background, (0,0))
        game_display.blit(sprites.cloud, (cloud_x,cloud_y))
        if cloud_x <= 800 - 1100:
            cloud_x=800
            cloud_y = random.randint(0, 400)
        else:
            if not player.wreck_start:
                cloud_x -= 5
            if godmode:
                title = message_to_screen("JET (GODMODE)", font, 80, yellow)
            else:
                title = message_to_screen("JET", font, 100, black)

            controls_1 = message_to_screen("USE WASD, SPACE PARA ATIRAR", font, 30, black)
            controls_2 = message_to_screen("USE SHIFT PARA JOGAR BOMBA, P PAUSAR", font, 30, black)

            if (selected) == "JOGAR":
                play = message_to_screen("JOGAR", font, 75, white)
            else:
                play = message_to_screen("JOGAR", font, 75, black)

            if (selected) == "SAIR":
                game_quit = message_to_screen("SAIR", font, 75, white)
            else:
                game_quit = message_to_screen("SAIR", font, 75, black)

                title_rect = title.get_rect()
                controls_1_rect = controls_1.get_rect()

                controls_2_rect = controls_2.get_rect()
                play_rect = play.get_rect()
                game_quit_rect = game_quit.get_rect()

                game_display.blit(title, (display_width/2 - (title_rect[2]/2),40))

                game_display.blit(controls_1, (display_width/2 - (controls_1_rect[2]/2),120))
                game_display.blit(controls_2, (display_width/2 - (controls_2_rect[2]/2),140)) 
                game_display.blit(play, (display_width/2 - (play_rect[2]/2), 200))
                game_display.blit(game_quit, (display_width/2 - (game_quit_rect[2]/2), 200))

                # Desenhando  o oceano
                pygame.draw.rect(game_display, blue, (0, 500, 800, 100))

                pygame.display.update()
                pygame.display.set_caption("VELOCIDADE DO JET" + str(int(clock.get_fps())) + "POR SEGUNDO")
                clock.tick(FPS)
