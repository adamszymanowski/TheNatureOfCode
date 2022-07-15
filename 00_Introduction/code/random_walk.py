import random

import pyray
from code.world_dimensions import center, scale, Point, in_bounds

class RandomWalk():
    def __init__(self):
        self.current_location = Point(center, center)
        self.previous_locations = []

    def draw(self):
        for location in self.previous_locations:
            x,y  = location
            pyray.draw_rectangle(x, y, scale, scale, pyray.BLACK)
        
        pyray.draw_rectangle(self.current_location.x, self.current_location.y, 
                                scale, scale, pyray.MAGENTA)

    def walk(self):
        location = Point(self.current_location.x, self.current_location.y)
        x_and_y = (location.x, location.y)
        if x_and_y not in self.previous_locations:
            self.previous_locations.append(x_and_y)

        r = random.randrange(4)
        # 0 Up 1 Down 2 Left 3 Right
        if r == 0:
            new_x = location.x + scale
            if in_bounds(new_x):
                self.current_location.x = new_x
        if r == 1:
            new_x = location.x - scale
            if in_bounds(new_x):
                self.current_location.x = new_x
        if r == 2:
            new_y = location.y + scale
            if in_bounds(new_y):
                self.current_location.y = new_y
        if r == 3:
            new_y = location.y - scale
            if in_bounds(new_y):
                self.current_location.y = new_y
        
