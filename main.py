import pygame

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

# Tile class
class Tile:
    def __init__(self, pos_x, pos_y, size=TILE_SIZE):
        self.nw = [pos_x, pos_y]
        self.ne = [pos_x, pos_y + size]
        self.sw = [pos_x + size, pos_y]
        self.se = [pos_x + size, pos_y + size]
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
def rotate_grid(angle_in_rads: float) -> None:
    pass

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

            tile.nw[0] += self.camera[0]
            tile.ne[0] += self.camera[0]
            tile.sw[0] += self.camera[0]
            tile.se[0] += self.camera[0]

            tile.nw[1] += self.camera[1]
            tile.ne[1] += self.camera[1]
            tile.sw[1] += self.camera[1]
            tile.se[1] += self.camera[1]
            if index % 2 == 0:
                # pygame.draw.rect(self.screen, GREEN, tile.rect)
                pygame.draw.lines(self.screen, GREEN, True, [tile.nw, tile.ne, tile.se, tile.sw]) 
            else:
                # pygame.draw.rect(self.screen, RED, tile.rect)
                pygame.draw.lines(self.screen, RED, True, [tile.nw, tile.ne, tile.se, tile.sw]) 
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
                        """
                    elif event.key == pygame.K_a:
                        # print("Pressed a!")
                        self.camera[0] -= 10
                    elif event.key == pygame.K_d:
                        # print("Pressed d!")
                        self.camera[0] += 10
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

