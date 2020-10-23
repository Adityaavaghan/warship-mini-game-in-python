import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("space war")
icon = pygame.image.load("countdown.png")
pygame.display.set_icon(icon)

# background = same as of icon variable line

playerimg = pygame.image.load("ufo.png")
px = 370
py = 480
px_change = 0

# multiplesenemy
enemy = []
ex = []
ey = []
ex_change = []
ey_change = []
numofene = 8
for i in range(numofene):
    enemy.append(pygame.image.load("spaceship.png"))
    ex.append(random.randint(0, 800))
    ey.append(random.randint(25, 125))
    ex_change.append(0.1)
    ey_change.append(40)

bullet = pygame.image.load("bullet.png")
bx = 0
by = 480
bx_change = 0
by_change = 10
b_state = "ready"

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textx = 10
texty = 10

gm = pygame.font.Font("freesansbold.ttf", 64)


def show(x, y):
    sco = font.render("score:" + str(score), True, (255, 255, 255))
    screen.blit(sco, (x, y))


def game_over_text():
    sca = gm.render("GAME OVER", True, (255, 255, 255))
    screen.blit(sca, (200, 250))


def player(x, y):
    screen.blit(playerimg, (x, y))


def ene(x, y, i):
    screen.blit(enemy[i], (x, y))


def bull(x, y):
    global b_state
    b_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))


def coll(ex, ey, bx, by):
    dist = (math.sqrt(math.pow(ex - bx, 2)) + (math.pow(ey - by, 2)))
    if dist < 27:
        return True
    else:
        return False


runn = True
while runn:

    screen.fill((49, 0, 0))
    # screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                px_change = -0.2

            if event.key == pygame.K_RIGHT:
                px_change = 0.2

            if event.key == pygame.K_SPACE:
                if b_state is "ready":
                    bx = px
                    bull(px, by)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                px_change = 0

    px += px_change
    if px <= 0:
        px = 0
    elif px >= 736:  # 800-64(spaceshipiconsize)
        px = 736

    for i in range(numofene):

        if ey[i] > 440:
            for j in range(numofene):
                ey[j] = 2000
            game_over_text()
            break

        ex[i] += ex_change[i]
        if ex[i] <= 0:
            ex_change[i] = 0.3
            ey[i] += ey_change[i]
        elif ex[i] >= 736:  # 800-64(spaceshipiconsize)
            ex_change[i] = -0.3
            ey[i] += ey_change[i]

        # collision
        collision = coll(ex[i], ey[i], bx, by)
        if collision:
            by = 480
            b_state = "ready"
            score += 1
            ex[i] = random.randint(0, 800)
            ey[i] = random.randint(25, 125)

        ene(ex[i], ey[i], i)

        if by <= 0:
            by = 480
            b_state = "ready"
        if b_state is "fire":
            bull(px, by)
            by -= by_change

    player(px, py)
    show(textx, texty)
    pygame.display.update()
