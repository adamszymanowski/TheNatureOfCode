window_size = 720
scale = 3
center = int(window_size / 2)
one_third = window_size / 3

def in_bounds(coord):
    return coord >= 0 and coord <= window_size

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
