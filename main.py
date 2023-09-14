''' 
Notes: Tetris specification

Block_Size = 4 units
Game_width = 10 units
Game_height = 20 units


'''

'''     CODE    '''

import pygame
import random

pygame.font.init()


# MASTER VARIABLES
s_width = 800
s_height = 700
play_width = 300
play_height = 600
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height




shapes = ['Q', 'Z', 'S', 'T', 'I', 'L', 'J']

class Piece(object):
    def __init__(self, x , y, shape) -> None:
        self.x = x
        self.y = y
        self.shape = shape

    
def create_grid(locked_pos = {}):
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid


def get_shape():
    return random.choice(shapes)






def draw_grid(surface, grid):

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size,  block_size, block_size), 0)

    pygame.display.rect(surface, (255,0,0),(top_left_x,top_left_y,play_width, play_height), 4)

    

def draw_window(surface,grid):
    surface.fill((0,0,0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255,255,255))

    surface.blit(label,(top_left_x + play_width/2 - (label.get_width()/2), 30))
    draw_grid(surface, grid)
    pygame.display.update()

def valid_space():
    pass


def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0


    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   current_piece -= 1
                   if not(valid_space(current_piece, grid)):     
                        current_piece += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x -= 1  

                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece -= 1  
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -= 1  
    draw_window(win,grid)

        


def main_menu(win):
    main(win)


win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)