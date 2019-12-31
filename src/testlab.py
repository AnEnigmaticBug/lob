from collections import namedtuple
from math import cos, sin, inf
from pie import Pie
from vec import Vec

gravity = Vec(0, 0.4)

TestLabParams = namedtuple('TestLabParams', ['anchor', 'target', 'world_bounds'])

class TestLab:
    def __init__(self, params, arm, pie):
        self.arm = arm
        self.pie = pie
        self.anchor = params.anchor
        self.target = params.target
        self.world_bounds = params.world_bounds
        self.time_elapsed = 0
        self.min_distance = inf
        self.holding_pie = False
    
    def update(self):
        self.holding_pie = False
        tip_vel = Vec(0, 0)
        tip_pos = self.anchor

        for rod in self.arm.rods:
            tip_vel.x += rod.length * rod.ang_vel * cos(rod.ang_pos)
            tip_vel.y -= rod.length * rod.ang_vel * sin(rod.ang_pos)
            tip_pos += Vec(rod.length * sin(rod.ang_pos), rod.length * cos(rod.ang_pos))

            if self.time_elapsed >= rod.boost_begin and rod.boost_count > 0:
                rod.ang_vel += rod.ang_acc
                rod.ang_pos += rod.ang_vel
                rod.boost_count -= 1
            else:
                rod.ang_vel -= 3 * gravity.y * sin(rod.ang_pos) / rod.length
                rod.ang_vel *= 0.98
                rod.ang_pos += rod.ang_vel
            
            if rod.boost_count > 0:
                self.holding_pie = True
        
        if self.holding_pie:
            self.pie.vel = tip_vel
            self.pie.pos = tip_pos
        else:
            self.pie.vel += gravity
            self.pie.pos += self.pie.vel
            
            self.min_distance = min(self.min_distance, (self.pie.pos - self.target).magnitude())
        
        self.time_elapsed += 1
    
    def has_ended(self):
        return not self.holding_pie and (
            self.pie.pos.x < 0 or
            self.pie.pos.y < 0 or
            self.pie.pos.x > self.world_bounds.x or
            self.pie.pos.y > self.world_bounds.y
        )
    
    def reset_arm(self, arm):
        self.arm = arm
        self.pie = Pie()
        self.time_elapsed = 0
        self.min_distance = inf
