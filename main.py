import pygame

# Engine variables
RES_HEIGHT = 800
RES_WIDTH = 600

# Some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating test grid
def create_grid(height: int, width: int) -> list:
    pass

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

    def run(self):
        self.main_game_loop()

    def main_game_loop(self):
        while self.game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_loop = False
            # Render frame here
            self.screen.fill(BLACK)

            # Do at the end of frame
            pygame.display.update()


if __name__ == "__main__":
    e = Engine(RES_HEIGHT, RES_WIDTH)
    e.run()

