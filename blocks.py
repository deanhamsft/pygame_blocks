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
        self.image = pygame.image.load(image_name).convert()
        self.rect = self.image.get_rect()
        self.score = score

class Quaterback(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("quarterback.png").convert()
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

pygame.init()


screen = pygame.display.set_mode(DIMENSIONS)
field_group = pygame.sprite.Group()
all_defenders = pygame.sprite.Group()
quaterback_group = pygame.sprite.Group()

for i in range(0, 50):
    defender = Defender("defender.png", -10)
    defender.rect.x = random.randrange(0, DIMENSIONS[0])
    defender.rect.y = random.randrange(0, DIMENSIONS[1])
    all_defenders.add(defender)

for i in range(0, 50):
    defender = Defender("offense.png", 10)
    defender.rect.x = random.randrange(0, DIMENSIONS[0])
    defender.rect.y = random.randrange(0, DIMENSIONS[1])
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
