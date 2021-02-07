import pygame


pygame.init()

# С помощью FPS контролируется скорость работы программы.
FPS = 170
# Создание окна
width = 500
height = 500
win = pygame.display.set_mode((width, height))
# Переменная clock, необходимая работы с FPS
clock = pygame.time.Clock()
pygame.display.set_caption('Шарик')

# Словарь, в котором содержатся значения, описывающие объект. 
# Некоторые значения можно задавать с помощью randint().
values = {'x_1': 100, 'y_1': 250, 'dir_1_x': 1, 'dir_1_y': 1, 'r_1': 25}

# Главный цикл (mainloop)
while True:
    # Проверка на нажатие крестика
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Проверяем, произошло ли 'касание' фигуры с левой и правой 
    # вертикальной гранями.
    if values['x_1'] > width - values['r_1'] or values['x_1'] < values['r_1']:
        # Меняем направление движения фигуры.
        values['dir_1_x'] = -values['dir_1_x']
    # То же самое для верхней и нижней граней.
    if values['y_1'] > height - values['r_1'] or values['y_1'] < values['r_1']:
        values['dir_1_y'] = -values['dir_1_y']
    # Изменение координат фигуры, то есть перемещение.
    values['x_1'] += values['dir_1_x']
    values['y_1'] += values['dir_1_y']
    # Закраска фона
    win.fill((255, 255, 255))
    # Построение окружности: задание цвета как переменной, 
    # а не как кортежа, позволит менять цвет окружности, при столкновении с гранями.
    pygame.draw.circle(win, (0, 255, 255), (values['x_1'], values['y_1']), values['r_1'])
    # Обновление экрана
    pygame.display.update()
    # Контроль FPS
    clock.tick(FPS)