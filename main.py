import pygame
import random

pygame.init()


height_sc = 500
width_sc = 500

FPS = 120
win = pygame.display.set_mode((width_sc, height_sc))
clock = pygame.time.Clock()
pygame.display.set_caption('Проверочная')

r = 25
height = 2 * r
width = 2 * r
h = 25
w = 50
x2 = random.randint(0, 400)
y2 = random.randint(0, 400)
color2 = (0, 188, 255)

x = 100
y = 50

x_step = 5
y_step = 5
color = (244, 45, 87)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= x_step
    elif keys[pygame.K_d]:
        x += x_step
    elif keys[pygame.K_w]:
        y -= y_step
    elif keys[pygame.K_s]:
        y += y_step
    elif keys[pygame.K_SPACE]:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    
            
    
    if x > width_sc:
        x = - width
    elif x < - width:
        x = width_sc

    elif y > height_sc:
        y = - height
    elif y < - height:
        y = height_sc
    
    win.fill((0, 125, 255))
    
    pygame.draw.circle(win, color, (x, y), r)
    pygame.draw.rect(win, color2, (x2, y2, h, w))

    if r == h or r == w:
        x2 == random.randint(0, 400)
        y2 == random.randint(0, 400)


    pygame.display.update()
    
    clock.tick(FPS)