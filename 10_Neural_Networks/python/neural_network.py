import pyray as pr
import utility as ut
import training as tr
from perceptron import Perceptron

ptron = Perceptron()
points = [tr.Point() for p in range(480)]

# Drawing
pr.init_window(ut.window_size, ut.window_size, "Neural Network")
pr.set_target_fps(6)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)


    for p in points:
        p.draw_point()
        p.draw_guess(ptron.guess(p.data))
        # pause
        if not pr.is_key_down(pr.KEY_DOWN):
            ptron.train(p)

    # Line dividing points (target)
    tr.draw_target_line_function()

    # Guess line
    ptron.draw_guess_line_function()

    pr.end_drawing()

    # quit
    if pr.is_key_down(pr.KEY_UP):
        break

pr.close_window()
