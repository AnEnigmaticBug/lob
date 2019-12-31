import pygame
from arm import Arm
from painter import Painter
from pie import Pie
from rod import Rod
from testlab import TestLab, TestLabParams
from vec import Vec

SCREEN_SIZE = 640

pygame.init()

testlab_params = TestLabParams(
    anchor=Vec(50, SCREEN_SIZE / 2),
    target=Vec(SCREEN_SIZE - 40, SCREEN_SIZE / 2),
    world_bounds=Vec(SCREEN_SIZE, SCREEN_SIZE)
)
testlab = TestLab(
    testlab_params,
    Arm([Rod(80, 10, 10, 0.01), Rod(80, 10, 10, 0.02)]),
    Pie(),
)
painter = Painter(pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE)))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    testlab.update()
    painter.paint(testlab)

    clock.tick(60)
