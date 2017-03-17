import pygame
import sys
import random

class Defender(pygame.sprite.Sprite):
    def __init__(self, image_name, score):
        super().__init__()
        self.image = pygame.image.load(image_name).convert()
        self.rect = self.image.get_rect()
        self.score = score

class Quaterback(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player_left.png").convert()
        self.rect = self.image.get_rect()
        self.score = 0

    def move_up(self):
        self.rect.y -= 1

    def move_down(self):
        self.rect.y += 1
        pass

    def move_left(self):
        self.rect.x -= 1
        pass

    def move_right(self):
        self.rect.x += 1
        pass

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

dimensions = (320, 240)
screen = pygame.display.set_mode(dimensions)
all_defenders = pygame.sprite.Group()
quaterback_group = pygame.sprite.Group()

for i in range(0, 50):
    defender = Defender("red_shroom.png", -10)
    defender.rect.x = random.randrange(0, 320)
    defender.rect.y = random.randrange(0, 240)
    all_defenders.add(defender)

for i in range(0, 50):
    defender = Defender("green_shroom.png", 10)
    defender.rect.x = random.randrange(0, 320)
    defender.rect.y = random.randrange(0, 240)
    all_defenders.add(defender)

quaterback = Quaterback()
quaterback.rect.x = 160
quaterback.rect.y = 120
quaterback_group.add(quaterback)

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
        quaterback.move_left()
    elif keys_pressed[pygame.K_d]:
        quaterback.move_right()
    
    if keys_pressed[pygame.K_w]:
        quaterback.move_up()
    elif keys_pressed[pygame.K_s]:
        quaterback.move_down()

    defenders_hit_list = pygame.sprite.spritecollide(quaterback, all_defenders, True)
    for defender in defenders_hit_list:
        quaterback.score += defender.score
        defender.kill()

    screen.fill(BLACK)
    all_defenders.draw(screen)
    quaterback_group.draw(screen)

    score_label = score_font.render("Score: {}".format(quaterback.score), 1, WHITE)
    screen.blit(score_label, (160 - score_label.get_rect().width / 2, 10))

    pygame.display.flip()
