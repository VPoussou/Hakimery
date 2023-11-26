
# So we do the Riemann thingy, which means we have a function
# It also means we have an interval with a beginning and an end
# Those would be the input, and the expected output is a number, a float
# Oh I forgot what the number of steps is, could be an input, could be fixed
# So then we need to kinda build the rectangles : 
# Their width would be equal to the interval size / number of steps
# Then for their height it requires evaluating the function for x = interval_size * current_step
# Now we have the rectangle surface area
# Then we just sum the shit out of those surface areas and we should be good

import typing
import math

def riemanization(function: typing.Callable, interval_start: float, interval_end: float, number_of_steps: bool) -> float:

    interval_size = interval_end - interval_start
    rectangle_width = interval_size / number_of_steps

    sum_of_areas = 0
    for current_step in range(number_of_steps):
        if current_step == 0:
            continue
        rectangle_height = function(interval_start + rectangle_width * current_step)
        rectangle_surface_area = rectangle_height * rectangle_width
        sum_of_areas += rectangle_surface_area

    return sum_of_areas

def test_function(x:float) -> float:
    return x**2 - 8 * math.log(x)

the_test = riemanization(test_function, 1, 3, 500000)
print(the_test)

the_test = riemanization()