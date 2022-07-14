import random
import pyray as pr
import utility as ut

class Perceptron():
    def __init__(self):
        self.weights = [0,0,0]
        self.learn_rate = 0.00025

        self.weights[0] = 1
        self.weights[1] = self.learn_rate # small value -> almost vertical slope 
        self.weights[2] = 1

        # inputs: (x,y,b) -> weights: (w0,w1,w2)
        # w0*x + w1*y + w2*b = 0
        # y = -((w0/w1) * x)  - (w2/w1) * b
        # y = m * x + b

    def m(self):
        # m = -((w0/w1)
        return -(self.weights[0]/self.weights[1])

    def b(self):
        # b = -(w2/w1) 
        return -(self.weights[2]/self.weights[1])

    def line_func(self, x):
        return  self.m() * x + self.b()

    def guess(self, inputs):
        s = sum([(i * w) for (i,w) in zip(inputs, self.weights)])
        return sign(s)

    def train(self, point):
        inputs = point.data
        guess_error =  point.label - self.guess(inputs)
        self.weights = [(w + (guess_error * i * self.learn_rate)) for (i,w) in zip(inputs, self.weights)]

    def draw_guess_line_function(self):
        x0 = -1.0
        x1 = 1.0
        color = pr.VIOLET
        pr.draw_line_ex(
                [ut.denormalize_x(x0), ut.denormalize_y(self.line_func(x0))],
                [ut.denormalize_x(x1), ut.denormalize_y(self.line_func(x1))],
                 5.0, color)
        # some style for better visibility?
        pr.draw_line_ex(
                [ut.denormalize_x(x0), ut.denormalize_y(self.line_func(x0))],
                [ut.denormalize_x(x1), ut.denormalize_y(self.line_func(x1))],
                 1.0, pr.PURPLE)
        # also draw equation
        m = self.m()
        b = self.b()
        o = "+ " if b > 0 else "" # adjust operator
        pr.draw_text(f"y = {m:.3f}x {o}{b:.3f}", 
                int(ut.window_size*(1/12)), int(ut.window_size*(2/12)), 48, color)

# activation function
def sign(n):
    if n >= 0:
        return 1
    else:
        return -1
