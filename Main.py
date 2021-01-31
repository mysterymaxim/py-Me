import pygame


pygame.init()

Weight = 500
Height = 500
x = 200
y = 200
x2 = 250
y2 = 250

win = pygame.display.set_mode((Weight, Height))
fps = pygame.time.Clock()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    Color2 = (24, 105, 255)
    Color1 = (255, 208, 24)
    win.fill((24, 255, 184))

    pygame.draw.rect(win, Color1, (x, y, 100, 100))
    pygame.draw.circle(win, Color2, (x2, y2), 25)

    pygame.display.update()

    x += 1
    if x > Weight:
        x = - 100

    # y2 -= 1
    # d

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] != 0:
        y2 -= 3
    if keys[pygame.K_a] != 0:
        x2 -= 3
    if keys[pygame.K_s] != 0:
        y2 += 3
    if keys[pygame.K_d] != 0:
        x2 += 3

    fps.tick(100)