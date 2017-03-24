import pygame
import sys
import random
import time

class Move():
    def __init__(self):
        pass

    def move_up(self):
        self.rect.y -= 1
        pass

    def move_down(self):
        self.rect.y += 1
        pass

    def move_left(self):
        self.rect.x -= 1
        pass

    def move_right(self):
        self.rect.x += 1
        pass

class Defender(pygame.sprite.Sprite):
    def __init__(self, image_name, score):
        super().__init__()
        self.image = pygame.image.load(image_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.score = score

class Quaterback(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("quarterback.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.score = 0

class Field(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("field.png").convert()
        self.rect = self.image.get_rect()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DIMENSIONS = (640, 480)
DEFENCE_FORMATION = {
    'corner1': [340, 80], 
    'corner2': [340, 400], 
    'o_line_back1': [330, 112], 
    'o_line_back2': [330, 368], 
    'end1': [330, 144], 
    'end2': [330, 336], 
    'tackle1': [330, 176], 
    'tackle2': [330, 304], 
    'middle_linebacker': [330, 208], 
    'safety1': [340, 176], 
    'safety2': [340, 304] 
    }

OFFENCE_POSITION = {
    'wide_receiver1': [290, 80], 
    'wide_receiver2': [290, 400],
    'tight_end': [300, 112], 
    'tackle1': [300, 368], 
    'tackle2': [300, 144], 
    'guard1': [300, 336], 
    'guard2': [300, 176], 
    'center': [300, 304], 
    'quarterback': [285, 208], 
    'fullback': [270, 208], 
    'halfback': [250, 208]    
    }

pygame.init()


screen = pygame.display.set_mode(DIMENSIONS)
field_group = pygame.sprite.Group()
all_defenders = pygame.sprite.Group()
quaterback_group = pygame.sprite.Group()

for v in DEFENCE_FORMATION.items():
    defender = Defender("defender.png", -10)
    defender.rect.x = v[1][0]
    defender.rect.y = v[1][1]
    all_defenders.add(defender)

for v in OFFENCE_POSITION.items():
    defender = Defender("offense.png", 10)
    defender.rect.x = v[1][0]
    defender.rect.y = v[1][1]
    all_defenders.add(defender)

field = Field()
field.rect.x = 0
field.rect.y = 0
field_group.add(field)

quaterback = Quaterback()
quaterback.rect.x = DIMENSIONS[0] / 2
quaterback.rect.y = DIMENSIONS[1] / 2
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
        Move.move_left(quaterback)
    elif keys_pressed[pygame.K_d]:
        Move.move_right(quaterback)
    
    if keys_pressed[pygame.K_w]:
        Move.move_up(quaterback)
    elif keys_pressed[pygame.K_s]:
        Move.move_down(quaterback)

    defenders_hit_list = pygame.sprite.spritecollide(quaterback, all_defenders, True)
    for defender in defenders_hit_list:
        quaterback.score += defender.score
        defender.kill()
    

    screen.fill(BLACK)
    
    field_group.draw(screen)
    all_defenders.draw(screen)
    quaterback_group.draw(screen)

    score_label = score_font.render("Score: {}".format(quaterback.score), 1, WHITE)
    screen.blit(score_label, ((DIMENSIONS[0] / 2) - score_label.get_rect().width / 2, 10))

    pygame.display.flip()
