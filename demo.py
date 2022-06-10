import pygame
import sys

pygame.init()
WIDTH = 600
HEIGHT = 600
LINE_COLOR = (23, 145, 135)
BG_COLOR = (28, 170, 156)
ROWS = 3
COLUMNS = 3
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill(BG_COLOR)
start_pos_1 = (200, 0)
start_pos_2 = (400, 0)
start_pos_3 = (0, 200)
start_pos_4 = (0, 400)
end_pos_1 = (200, 0)
end_pos_2 = (400, 0)
end_pos_3 = (0, 200)
end_pos_4 = (0, 400)
highlight = (190, 220, 230)

#   main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    end_pos_1 = (end_pos_1[0], end_pos_1[1] + 0.2)
    end_pos_2 = (end_pos_2[0], end_pos_2[1] + 0.2)
    end_pos_3 = (end_pos_3[0] + 0.2, end_pos_3[1])
    end_pos_4 = (end_pos_4[0] + 0.2, end_pos_4[1])
    pygame.draw.line(screen, LINE_COLOR, start_pos_1, end_pos_1, 15)
    pygame.draw.line(screen, LINE_COLOR, start_pos_2, end_pos_2, 15)
    pygame.draw.line(screen, LINE_COLOR, start_pos_3, end_pos_3, 15)
    pygame.draw.line(screen, LINE_COLOR, start_pos_4, end_pos_4, 15)

    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(0, 0, 600, 600), 15)

    cursor = pygame.mouse.get_pos()
    if 0 <= cursor[0] <= 200 and 0 <= cursor[1] <= 200:
        pygame.draw.rect(screen, highlight, pygame.Rect(0, 0, 200, 200), 5)
    elif (200 <= cursor[0] <= 400) and 0 <= cursor[1] <= 200:
        pygame.draw.rect(screen, highlight, pygame.Rect(200, 0, 200, 200), 5)
    elif 400 <= cursor[0] <= 600 and 0 <= cursor[1] <= 200:
        pygame.draw.rect(screen, highlight, pygame.Rect(400, 0, 200, 200), 5)

    elif (0 <= cursor[0] <= 200) and 200 <= cursor[1] <= 400:
        pygame.draw.rect(screen, highlight, pygame.Rect(0, 200, 200, 200), 5)
    elif 200 <= cursor[0] <= 400 and 200 <= cursor[1] <= 400:
        pygame.draw.rect(screen, highlight, pygame.Rect(200, 200, 200, 200), 5)
    elif (400 <= cursor[0] <= 600) and 200 <= cursor[1] <= 400:
        pygame.draw.rect(screen, highlight, pygame.Rect(400, 200, 200, 200), 5)

    elif (0 <= cursor[0] <= 200) and 400 <= cursor[1] <= 600:
        pygame.draw.rect(screen, highlight, pygame.Rect(0, 400, 200, 200), 5)
    elif (200 <= cursor[0] <= 400) and 400 <= cursor[1] <= 600:
        pygame.draw.rect(screen, highlight, pygame.Rect(200, 400, 200, 200), 5)
    elif (400 <= cursor[0] <= 600) and 400 <= cursor[1] <= 600:
        pygame.draw.rect(screen, highlight, pygame.Rect(400, 400, 200, 200), 5)