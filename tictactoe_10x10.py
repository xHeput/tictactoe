import pygame
from pygame.locals import *


def tictactoe_grid():
    background_color = (255, 255, 255)
    axes_color = (0, 0, 0)
    screen.fill(background_color)
    for i in range(1, 10):
        # poziome osie, horizontal axes
        pygame.draw.line(screen, axes_color, (0, i * 50), (game_width, i * 50))
        # pionowe osie, vertical axes
        pygame.draw.line(screen, axes_color, (i * 50, 0), (i * 50, game_width))


red = (255, 0, 0)
blue = (0, 0, 255)


def draw_player_move():
    x_pos = 0
    for x in container:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, red, (x_pos * 50 + 10, y_pos * 50 + 10), (x_pos * 50 + 40, y_pos * 50 + 40), 10)
                pygame.draw.line(screen, red, (x_pos * 50 + 10, y_pos * 50 + 40), (x_pos * 50 + 40, y_pos * 50 + 10), 10)
            if y == -1:
                pygame.draw.circle(screen, blue, (x_pos * 50 + 25, y_pos * 50 + 25), 10)
            y_pos += 1
        x_pos += 1


pygame.init()
# game screen settings
game_width = 500
game_height = 500

screen = pygame.display.set_mode((game_height, game_width))
pygame.display.set_caption('TicTacToe_10x10 - 5 in a row wins!')

container = []
for n in range(10):
    row = [0] * 10
    container.append(row)
print(container)


game_status = True
clicked = False
mouse_pos = []
player = 1
while game_status:
    tictactoe_grid()
    draw_player_move()
    # events detections
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            mouse_pos = pygame.mouse.get_pos()
            cell_x = mouse_pos[0]
            cell_y = mouse_pos[1]
            if container[cell_x // 50][cell_y // 50] == 0:
                container[cell_x // 50][cell_y // 50] = player
                player *= -1
    # updates all the changes in the game
    pygame.display.update()

pygame.quit()
