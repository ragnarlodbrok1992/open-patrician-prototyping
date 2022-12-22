import pygame
from math import sin, cos

# Engine variables
RES_HEIGHT = 800
RES_WIDTH = 600

# Grid values
TILE_SIZE = 20
GRID_ROWS = 21
GRID_COLUMNS = 30 

# Some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# <------y------->
# ^
# -
# x
# -
# v

# Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_pair(self):
        return (self.x, self.y)

# Tile class
class Tile:
    def __init__(self, pos_x, pos_y, size=TILE_SIZE):
        self.nw = Point(pos_x, pos_y)
        self.ne = Point(pos_x, pos_y + size)
        self.sw = Point(pos_x + size, pos_y)
        self.se = Point(pos_x + size, pos_y + size)

        # DEBUG
        # self.nw = [pos_x, pos_y]
        # self.ne = [pos_x, pos_y + size]
        # self.sw = [pos_x + size, pos_y]
        # self.se = [pos_x + size, pos_y + size]
        # self.rect = pygame.Rect(self.nw, (size, size))

        # DEBUG
        # print(self.nw)
        # print(self.ne)
        # print(self.sw)
        # print(self.se)
        # print(self.rect)


# Creating test grid
def create_grid(height: int, width: int) -> list:
    grid_output = []
    for x in range(0, height):
        for y in range(0, width):
            grid_output.append(Tile(x * TILE_SIZE, y * TILE_SIZE))
    return grid_output

# Prototyping functions - rotating grid
def rotate_grid(angle_in_rads: float, grid: list) -> None:
    ROTATION_MATRIX = [[cos(angle_in_rads), -sin(angle_in_rads)], [sin(angle_in_rads), cos(angle_in_rads)]]
    print(ROTATION_MATRIX)

# Prototyping functions - tilting camera
def tilt_camera(angle_in_rads: float) -> None:
    pass

class Engine():

    def __init__(self, res_height: int , res_width: int) -> None:
        pygame.init()
        pygame.display.set_caption("Open Patrician Prototyping engine")
        self.screen = pygame.display.set_mode((res_height, res_width))
        self.game_loop = True

        # Prototyping variables
        self.camera = [0, 0]
        self.grid = create_grid(GRID_COLUMNS, GRID_ROWS)
        self.left_mouse_button_held = False
        self.radians = 0.0

        # Debug
        # Tile(0, 0)
        # print(self.grid)

    def run(self):
        self.main_game_loop()

    def render_grid(self):
        # Render grid
        for index, tile in enumerate(self.grid):
            # Change rects positions
            # tile.rect.move_ip(self.camera[0], self.camera[1])

            tile.nw.x += self.camera[0]
            tile.ne.x += self.camera[0]
            tile.sw.x += self.camera[0]
            tile.se.x += self.camera[0]

            tile.nw.y += self.camera[1]
            tile.ne.y += self.camera[1]
            tile.sw.y += self.camera[1]
            tile.se.y += self.camera[1]
            if index % 2 == 0:
                # pygame.draw.rect(self.screen, GREEN, tile.rect)
                pygame.draw.lines(self.screen, GREEN, True, [tile.nw.get_pair(), tile.ne.get_pair(), tile.se.get_pair(), tile.sw.get_pair()]) 
            else:
                # pygame.draw.rect(self.screen, RED, tile.rect)
                pygame.draw.lines(self.screen, RED, True, [tile.nw.get_pair(), tile.ne.get_pair(), tile.se.get_pair(), tile.sw.get_pair()]) 
        # Zero the camera
        self.camera = [0, 0]

    def main_game_loop(self):
        while self.game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_loop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        self.game_loop = False
                    elif event.key == pygame.K_q:
                        self.radians -= 0.1
                        rotate_grid(self.radians, self.grid)
                    elif event.key == pygame.K_e:
                        self.radians += 0.1
                        rotate_grid(self.radians, self.grid)
                        """
                    elif event.key == pygame.K_w:
                        # print("Pressed w!")
                        self.camera[1] -= 10
                    elif event.key == pygame.K_s:
                        # print("Pressed s!")
                        self.camera[1] += 10
                        """
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pressed_keys = pygame.mouse.get_pressed()
                    self.left_mouse_button_held = mouse_pressed_keys[0]
                    # mouse_pos_rel = pygame.mouse.get_rel()
                    print(mouse_pressed_keys)
                    # print(mouse_pos_rel)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.left_mouse_button_held = False
            # Check if mouse button is held
            if self.left_mouse_button_held:
                # print("Holding left mouse button!")
                # print(pygame.mouse.get_rel())
                mouse_rel = pygame.mouse.get_rel()
                self.camera[0] += mouse_rel[0]
                self.camera[1] += mouse_rel[1]
            else:
                pygame.mouse.get_rel()

            # Render frame here

            self.screen.fill(BLACK)

            # Render grid
            self.render_grid()

            # Do at the end of frame
            pygame.display.update()


if __name__ == "__main__":
    e = Engine(RES_HEIGHT, RES_WIDTH)
    e.run()

