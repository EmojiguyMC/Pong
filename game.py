import pygame
import random
from time import sleep as s
pygame.init()
font = pygame.font.SysFont("Minecraft", 25, bold=True)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
running = True
p1 = 25
p2 = 25
vel = [0,0]
winner = 0
ball = [390, 290]


def closecode():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

type = 0

while running:
    closecode()
    if pygame.key.get_pressed()[pygame.K_1]:
        type = 1
        winner = 0
        ball = [395,295]
        rand = random.randint(1,4)
        if rand == 1:
            vel = [3, 3]
        if rand == 2:
            vel = [-3, 3]
        if rand == 3:
            vel = [-3, -3]
        if rand == 4:
            vel = [3, -3]
    if pygame.key.get_pressed()[pygame.K_2]:
        type = 2
        winner = 0
        ball = [395,295]
        rand = random.randint(1,4)
        if rand == 1:
            vel = [3, 3]
        if rand == 2:
            vel = [-3, 3]
        if rand == 3:
            vel = [-3, -3]
        if rand == 4:
            vel = [3, -3]
    #background
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
    pygame.draw.rect(screen, (255, 255, 255), (5, 5, 790, 590), 2)
    #p1 controls
    if pygame.key.get_pressed()[pygame.K_w]:
        p1 -= .5 * clock.get_time()
    if pygame.key.get_pressed()[pygame.K_s]:
        p1 += .5 * clock.get_time()
    if p1 + 50 >= 600:
        p1 = 550
    if p1 <= 0:
        p1 = 0
    #p2 controls
    if type == 1:
         if pygame.key.get_pressed()[pygame.K_UP]:
            p2 -= .5 * clock.get_time()
         if pygame.key.get_pressed()[pygame.K_DOWN]:
            p2 += .5 * clock.get_time()
         if p2 + 50 >= 600:
            p2 = 550
         if p2 <= 0:
            p2 = 0
    if type == 2:
        p2 = ball[1] - 20

    #drawing pongs on screen
    pygame.draw.rect(screen, (255, 255, 255), (25, p1, 10, 50))
    pygame.draw.rect(screen, (255, 255, 255), (765, p2, 10, 50))

    mp = font.render("Press 1 for multiplayer, 2 for singleplayer.", False, (255, 255, 255))
    screen.blit(mp, (20,560))

    #ball code
    pygame.draw.ellipse(screen, (255, 255, 255), (ball[0], ball[1], 10, 10))
    
    ball[0] += vel[0]
    ball[1] += vel[1]

    if ball[1] + 10 >= 600:
        vel[1] *= -1
    if ball[0] + 10 >= 800:
        vel[0] *= -1
        winner = 1
    if ball[1] <= 0:
        vel[1] *= -1
    if ball[0] <= 0:
        vel[0] *= -1
        winner = 2
        
    if ball[0] - 10 <= 25:
        if p1 <= ball[1] <= p1 + 50:
            vel[0] *= -1.02
    if ball[0] + 10 >= 765:
        if p2 <= ball[1] <= p2 + 50:
            vel[0] *= -1.02
    if winner == 1:
        pygame.draw.rect(screen,(0,0,0),(0,0,800,600))
        p1w = font.render("Player 1 Wins!", False, (255, 255, 255))
        screen.blit(p1w, (300,300))
    if winner == 2:
        pygame.draw.rect(screen,(0,0,0),(0,0,800,600))
        p2w = font.render("Player 2 Wins!", False, (255, 255, 255))
        screen.blit(p2w, (300,300))
    pygame.display.update()
    clock.tick(60)