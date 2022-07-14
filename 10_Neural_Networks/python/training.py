import pyray as pr
import utility as ut
import random

m = random.uniform(-0.5, 0.5)
b = random.uniform(-0.5, 0.5)

def line_func(x):
    # y = m * x + b
    return  m * x + b 

def draw_target_line_function():
    x0 = -1.0
    x1 = 1.0
    color = pr.LIME
    pr.draw_line_ex(
            [ut.denormalize_x(x0), ut.denormalize_y(line_func(x0))],
            [ut.denormalize_x(x1), ut.denormalize_y(line_func(x1))],
             3.0, color)
    # some style for better visibility?
    pr.draw_line_ex(
            [ut.denormalize_x(x0), ut.denormalize_y(line_func(x0))],
            [ut.denormalize_x(x1), ut.denormalize_y(line_func(x1))],
             1.0, pr.GREEN)
    # also draw equation
    o = "+ " if b > 0 else "" # adjust operator
    pr.draw_text(f"y = {m:.3f}x {o}{b:.3f}", 
        int(ut.window_size*(1/12)), int(ut.window_size*(1/12)), 48, color)

class Point():
    def __init__(self):
        self.x = random.uniform(-1, 1)
        self.y = random.uniform(-1, 1)
        self.b = 1 # bias
        self.data = [self.x, self.y, self.b]

        if self.y > line_func(self.x):
            self.label = 1
        else:
            self.label = -1

        self.r = 9 # radius for drawing
        self.pixel_x = ut.denormalize_x(self.x)
        self.pixel_y = ut.denormalize_y(self.y)

    def draw_point(self):
        if self.label == 1:
            pr.draw_circle(self.pixel_x, self.pixel_y, self.r, pr.WHITE)
            pr.draw_circle_lines(self.pixel_x, self.pixel_y, self.r, pr.BLACK)
        else:
            pr.draw_circle(self.pixel_x, self.pixel_y, self.r, pr.DARKGRAY)
            pr.draw_circle_lines(self.pixel_x, self.pixel_y, self.r, pr.BLACK)

    def draw_guess(self, guess):
        s = 5
        if guess != self.label:
            pr.draw_circle(self.pixel_x, self.pixel_y, self.r-s, pr.GOLD)
