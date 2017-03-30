import pygame
import sys
import random
import time
import math

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

class Fire_Path():
    def __init__(self):
        pass

    def artilery(self, football):
        velx=math.cos(football.rect.x) * 10
        vely=math.sin(football.rect.y) * 10
        football.rect.x += velx
        football.rect.y += vely
        pass

class Defender(pygame.sprite.Sprite):
    def __init__(self, image_name, Offence):
        super().__init__()
        self.image = pygame.image.load(image_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.score = Offence

class Quarterback(pygame.sprite.Sprite):
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

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cross.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, pos):
        self.rect = pos

class Football(pygame.sprite.Sprite, rads):
    def __init__(self):
        super().__init__()
        rads = rads
        self.image = pygame.image.load("football.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, pos):
        velx=math.cos(self.rect.x) * 10
        vely=math.sin(self.rect.y) * 10
        self.rect.x += velx
        self.rect.y += vely
        self.rect = pos

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DIMENSIONS = (640, 480)
DEFENCE_FORMATION = {
    'corner1': [370, 80], 
    'o_line_back1': [355, 112], 
    'end1': [330, 144], 
    'tackle1': [330, 176], 
    'safety1': [355, 176], 
    'middle_linebacker': [330, 208], 
    'tackle2': [330, 240], 
    'safety2': [355, 240] ,
    'end2': [330, 272],
    'o_line_back2': [355, 304], 
    'corner2': [370, 336]
    }

OFFENCE_POSITION = {
    'wide_receiver1': [290, 80], 
    'tight_end': [300, 112], 
    'tackle2': [300, 144], 
    'guard2': [300, 176], 
    'fullback': [235, 208], 
    'halfback': [215, 208],  
    'center': [300, 240], 
    'guard1': [300, 272], 
    'tackle1': [300, 304], 
    'wide_receiver2': [290, 336]
    }

pygame.init()

pygame.mouse.set_visible ( False ) 
screen = pygame.display.set_mode(DIMENSIONS)
field_group = pygame.sprite.Group()
all_defenders = pygame.sprite.Group()
all_offence = pygame.sprite.Group()
quarterback_group = pygame.sprite.Group()
target_group = pygame.sprite.Group()
football_group = pygame.sprite.Group()

for v in DEFENCE_FORMATION.items():
    defender = Defender("defender.png", -10)
    defender.rect.x = v[1][0]
    defender.rect.y = v[1][1]
    all_defenders.add(defender)

for v in OFFENCE_POSITION.items():
    defender = Defender("offense.png", 10)
    defender.rect.x = v[1][0]
    defender.rect.y = v[1][1]
    all_offence.add(defender)

field = Field()
field.rect.x = 0
field.rect.y = 0
field_group.add(field)

quarterback = Quarterback()
quarterback.rect.x = 285
quarterback.rect.y = 208
quarterback_group.add(quarterback)

target = Crosshair()
target.rect = (0,0)
target_group.add(target)

football = Football(math.atan2(target.rect.y - quarterback.rect.y, target.rect.x - quarterback.rect.x))
football.rect = quarterback.rect
football_group.add(football)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            football.update()
            #go get some of the code from archer to do the football

    if keys_pressed[pygame.K_a]:
        Move.move_left(quaterback)
    elif keys_pressed[pygame.K_d]:
        Move.move_right(quaterback)
    
    if keys_pressed[pygame.K_w]:
        Move.move_up(quaterback)
    elif keys_pressed[pygame.K_s]:
        Move.move_down(quaterback)

    target_pos = pygame.mouse.get_pos()
    target.update(target_pos)


    defenders_hit_list = pygame.sprite.spritecollide(quarterback, all_defenders, True)
    for defender in defenders_hit_list:
        quaterback.score += defender.score
        defender.kill()
    
    #if football:
        #football.update()


    screen.fill(BLACK)

    field_group.draw(screen)
    all_defenders.draw(screen)
    all_offence.draw(screen)
    quarterback_group.draw(screen)
    target_group.draw(screen)
    football_group.draw(screen)

    score_label = score_font.render("Score: {}".format(quarterback.score), 1, WHITE)
    screen.blit(score_label, ((DIMENSIONS[0] / 2) - score_label.get_rect().width / 2, 10))

    pygame.display.flip()
