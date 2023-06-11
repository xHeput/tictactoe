import pygame
from pygame.locals import *
pygame.init()

def tictactoe_grid():
    background_color = (255, 255, 255)
    axes_color = (0, 0, 0)
    screen.fill(background_color)
    for i in range(1, 10):
        # poziome osie, horizontal axes
        pygame.draw.line(screen,
                         axes_color,
                         (0, i * 50),
                         (game_width, i * 50))
        # pionowe osie, vertical axes
        pygame.draw.line(screen,
                         axes_color,
                         (i * 50, 0),
                         (i * 50, game_width))


def draw_player_move():
    x_pos = 0
    for x in container:
        y_pos = 0
        for y in x:
            # definition of X
            if y == 1:
                pygame.draw.line(screen,
                                 red,
                                 (x_pos * 50 + 10, y_pos * 50 + 10),
                                 (x_pos * 50 + 40, y_pos * 50 + 40),
                                 10)
                pygame.draw.line(screen,
                                 red,
                                 (x_pos * 50 + 10, y_pos * 50 + 40),
                                 (x_pos * 50 + 40, y_pos * 50 + 10),
                                 10)
            if y == -1:
                # definition of Y
                pygame.draw.circle(screen,
                                   blue,
                                   (x_pos * 50 + 25, y_pos * 50 + 25),
                                   10)
            y_pos += 1
        x_pos += 1


def winner_checker():
    global winner
    global game_over
    y_pos = 0
    for x in container:
        # checking columns
        if sum(x) == 5:
            winner = 1
            game_over = True
        if sum(x) == -5:
            winner = -1
            game_over = True

    # checking rows
    if container[0][y_pos] + container[1][y_pos] + container[2][y_pos] + container[3][y_pos] + container[4][y_pos] == 5:
        winner = 1
        game_over = True
    if container[0][y_pos] + container[1][y_pos] + container[2][y_pos] + container[3][y_pos] + container[4][y_pos] == -5:
        winner = -1
        game_over = True
    y_pos += 1

    if check_diagonal_win(1):
        winner = 1
        game_over = True
    if check_diagonal_win(-1):
        winner = -1
        game_over = True


def check_diagonal_win(player_id):
    print("player to: ", player_id)
    # Sprawdzenie ukosów z lewej górnej do prawej dolnej
    for row_ in range(6):
        for col in range(6):
            if sum(container[row_ + i][col + i] == player for i in range(5)) == 5:
                return True

    # Sprawdzenie ukosów z lewej dolnej do prawej górnej
    for row_ in range(9, 3, -1):
        for col in range(6):
            if sum(container[row_ - i][col + i] == player for i in range(5)) == 5:
                return True

    return False


def draw_winner(winner):
    if winner == 1:
        text = font.render('Gracz X wygrywa!', True, blue)
    else:
        text = font.render('Gracz 0 wygrywa!', True, blue)

    pygame.draw.rect(screen, green, (game_width // 2 - 500, game_height // 2 - 350, 200, 50))
    screen.blit(text, (game_width // 2 - 500, game_height // 2 - 250))


# colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# fonts
font = pygame.font.Font(None, 10)
# variables
game_width = 500
game_height = 500
game_status = True
clicked = False
mouse_pos = []
player = 1
winner = 0
game_over = False


# game screen settings
screen = pygame.display.set_mode((game_height, game_width))
pygame.display.set_caption('TicTacToe_10x10 - 5 in a row wins!')

container = []
for n in range(10):
    row = [0] * 10
    container.append(row)
print(container)

while game_status:
    tictactoe_grid()
    draw_player_move()
    # events detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked is False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked is True:
                clicked = False
                mouse_pos = pygame.mouse.get_pos()
                cell_x = mouse_pos[0]
                cell_y = mouse_pos[1]
                if container[cell_x // 50][cell_y // 50] == 0:
                    container[cell_x // 50][cell_y // 50] = player
                    player *= -1
                    winner_checker()

    if game_over is True:
        draw_winner(winner)

    # updates all the changes in the game
    pygame.display.update()

pygame.quit()
