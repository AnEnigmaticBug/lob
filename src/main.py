import pygame
from arm import Arm
from conf import  generations, population_size, screen_size
from evolver import Evolver
from painter import Painter
from pie import Pie
from rod import Rod
from testlab import TestLab, TestLabParams
from vec import Vec

pygame.init()

testlab_params = TestLabParams(
    anchor=Vec(50, screen_size / 2),
    target=Vec(screen_size - 40, screen_size / 2),
    world_bounds=Vec(screen_size, screen_size)
)
evolver = Evolver(generations, population_size, testlab_params)
testlab = TestLab(
    testlab_params,
    evolver.evolve(),
    Pie(),
)
painter = Painter(pygame.display.set_mode((screen_size, screen_size)))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    testlab.update()
    painter.paint(testlab)

    clock.tick(60)
