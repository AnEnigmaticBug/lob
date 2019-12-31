import pygame
from math import cos, sin
from vec import Vec

ARM_COLOR = (225,  99,  99)
ARM_JOINT_COLOR = (  0,  68,  69)
BACK_DROP_COLOR = (110,  33,  66)
PIE_COLOR = (255, 214, 146)
TARGET_COLOR = (255, 255, 255)

class Painter:
    def __init__(self, screen):
        self.screen = screen
    
    def paint(self, lab):
        self.screen.fill(BACK_DROP_COLOR)

        arm_joint_positions = [lab.anchor]
        tip_pos1 = lab.anchor
        tip_pos2 = None

        for rod in lab.arm.rods:
            tip_pos2 = tip_pos1 + Vec(rod.length * sin(rod.ang_pos), rod.length * cos(rod.ang_pos))
            arm_joint_positions.append(tip_pos2)

            pygame.draw.line(self.screen, ARM_COLOR, (tip_pos1.x, tip_pos1.y), (tip_pos2.x, tip_pos2.y), width=8)

            tip_pos1 = tip_pos2
        
        for pos in arm_joint_positions:
            pygame.draw.circle(self.screen, ARM_JOINT_COLOR, (pos.x, pos.y), 10)

        pygame.draw.circle(self.screen, PIE_COLOR, (lab.pie.pos.x, lab.pie.pos.y), 10)
        pygame.draw.circle(self.screen, TARGET_COLOR, (lab.target.x, lab.target.y), 10)

        pygame.display.update()
