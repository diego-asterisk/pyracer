#!/usr/bin/env python3
import pygame
import sys
import random

ANCHO = 800
ALTO = 600
# tuplas
AREA = (ANCHO, ALTO)
COLOR_RUNNER = (255, 20, 100)
COLOR_ENEMY = []
COLOR_ENEMY.append((0, 200, 255))
COLOR_ENEMY.append((50, 100, 255))
COLOR_ENEMY.append((100, 50, 255))
COLOR_FONDO = (0, 0, 0)
DIMENSION = 50

# diccionarios
runner = {}
runner['x'] = ANCHO / 2
runner['y'] = ALTO - DIMENSION * 1.5
runner['color'] = COLOR_RUNNER

# qué pasaría si tuviera 2 enemigos? o un array?
sprites = []
sprites.append(runner)
enemigos = []
for i in range(8):
    enemigo = {}
    enemigo['x'] = random.randint(0, ANCHO - DIMENSION)
    enemigo['y'] = DIMENSION
    enemigo['color'] = COLOR_ENEMY[i % 3]
    enemigos.append(enemigo)
    sprites.append(enemigo)

FPS = 30
clock = pygame.time.Clock()


def draw(sprite):
    # objeto se dibuja
    estado = (sprite['x'], sprite['y'], DIMENSION, DIMENSION)
    pygame.draw.rect(ventana, sprite['color'], estado)


def drawer():
    ventana.fill(COLOR_FONDO)
    # iterar sobre la lista de sprites
    for sprite in sprites:
        draw(sprite)
    clock.tick(FPS)
    pygame.display.update()


def enemy_update(enemigos):
    puntos = 0
    for enemigo in enemigos:
        enemigo['y'] += random.randint(4, 12)
        if enemigo['y'] > ALTO:
            puntos += 1
            enemigo['y'] = DIMENSION
            enemigo['x'] = random.randint(0, ANCHO - DIMENSION)

    return puntos


def detectar_colision(runner, enemigos):
    for enemigo in enemigos:
        # primer dimension es la de runner y la segunda es del enemigo
        izq = enemigo['x'] - DIMENSION
        der = enemigo['x'] + DIMENSION
        if (runner['x'] >= izq and runner['x'] <= der):
            alto = enemigo['y'] - DIMENSION
            bajo = enemigo['y'] + DIMENSION
            if (runner['y'] >= alto and runner['y'] <= bajo):
                return True
    return False


ventana = pygame.display.set_mode(AREA)
score = 0
game_over = False
drawer()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                runner['x'] -= DIMENSION
            if event.key == pygame.K_RIGHT:
                runner['x'] += DIMENSION
            if event.key == pygame.K_ESCAPE:
                pygame.time.wait(250)
                game_over = True

    drawer()
    if detectar_colision(runner, enemigos):
        pygame.time.wait(1000)
        game_over = True
    score += enemy_update(enemigos)

print("\nScore: {}\nGAME OVER\n".format(score))
