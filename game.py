import pygame
import random

pygame.init()
font = pygame.font.SysFont("arial", 25, bold=True)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
running = True
p1 = 25
p2 = 25
vel = [3, 3]
ball = [390, 290]


def closecode():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()


while running:
    closecode()
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
    pygame.draw.rect(screen, (255, 255, 255), (5, 5, 790, 590), 2)
    #p1
    if pygame.key.get_pressed()[pygame.K_w]:
        p1 -= .5 * clock.get_time()
    if pygame.key.get_pressed()[pygame.K_s]:
        p1 += .5 * clock.get_time()
    if p1 + 50 >= 600:
        p1 = 550
    if p1 <= 0:
        p1 = 0
    #p2
    if pygame.key.get_pressed()[pygame.K_UP]:
        p2 -= .5 * clock.get_time()
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        p2 += .5 * clock.get_time()
    if p2 + 50 >= 600:
        p2 = 550
    if p2 <= 0:
        p2 = 0
    pygame.draw.rect(screen, (255, 255, 255), (25, p1, 10, 50))
    pygame.draw.rect(screen, (255, 255, 255), (765, p2, 10, 50))

    # mp = font.render("Multiplayer", False, (255, 255, 255))
    # screen.blit(mp, (400,300))

    pygame.draw.ellipse(screen, (255, 255, 255), (ball[0], ball[1], 10, 10))
    ball[0] += vel[0]
    ball[1] += vel[1]

    if ball[1] + 10 >= 600:
        vel[1] *= -1
    if ball[0] + 10 >= 800:
        vel[0] *= -1
    if ball[1] <= 0:
        vel[1] *= -1
    if ball[0] <= 0:
        vel[0] *= -1
    if ball[0] - 10 <= 25:
        if p1 <= ball[1] <= p1 + 50:
            vel[0] *= -1.02
    if ball[0] + 10 >= 765:
        if p2 <= ball[1] <= p2 + 50:
            vel[0] *= -1.02
    pygame.display.update()
    clock.tick(60)
