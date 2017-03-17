import pygame
import sys
import random

class Mushroom(pygame.sprite.Sprite):
    def __init__(self, image_name, score):
        super().__init__()
        self.image = pygame.image.load(image_name).convert()
        self.rect = self.image.get_rect()
        self.score = score

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player_left.png").convert()
        self.rect = self.image.get_rect()
        self.score = 0

    def move_up(self):
        self.rect.y -= 1

    def move_down(self):
        self.rect.y += 2
        pass

    def move_left(self):
        self.rect.x -= 2
        pass

    def move_right(self):
        self.rect.x += 2
        pass

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

dimensions = (320, 240)
screen = pygame.display.set_mode(dimensions)
all_mushrooms = pygame.sprite.Group()
player_group = pygame.sprite.Group()

for i in range(0, 50):
    mushroom = Mushroom("red_shroom.png", -10)
    mushroom.rect.x = random.randrange(0, 320)
    mushroom.rect.y = random.randrange(0, 240)
    all_mushrooms.add(mushroom)

for i in range(0, 50):
    mushroom = Mushroom("green_shroom.png", 10)
    mushroom.rect.x = random.randrange(0, 320)
    mushroom.rect.y = random.randrange(0, 240)
    all_mushrooms.add(mushroom)

player = Player()
player.rect.x = 160
player.rect.y = 120
player_group.add(player)

keys_pressed = { pygame.K_w: False, pygame.K_a: False, pygame.K_s: False, pygame.K_d: False }

score_font = pygame.font.SysFont("monospace", 15)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed[event.key] = False            

    if keys_pressed[pygame.K_a]:
        player.move_left()
    elif keys_pressed[pygame.K_d]:
        player.move_right()
    
    if keys_pressed[pygame.K_w]:
        player.move_up()
    elif keys_pressed[pygame.K_s]:
        player.move_down()

    mushrooms_hit_list = pygame.sprite.spritecollide(player, all_mushrooms, True)
    for mushroom in mushrooms_hit_list:
        player.score += mushroom.score
        mushroom.kill()

    screen.fill(BLACK)
    all_mushrooms.draw(screen)
    player_group.draw(screen)

    score_label = score_font.render("Score: {}".format(player.score), 1, WHITE)
    screen.blit(score_label, (160 - score_label.get_rect().width / 2, 10))

    pygame.display.flip()
