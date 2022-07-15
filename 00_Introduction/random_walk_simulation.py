import pyray
from code.world_dimensions import window_size, one_third
from code.random_walk import RandomWalk

# Setup
simulation = RandomWalk()

# Drawing
pyray.init_window(window_size, window_size, "Random Walk")
pyray.set_target_fps(60)

while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.clear_background(pyray.RAYWHITE)
    pyray.draw_rectangle_rec((one_third, one_third, one_third, one_third), pyray.WHITE)
    # Simulation
    simulation.draw()
    simulation.walk()
    pyray.end_drawing()

pyray.close_window()
