
import random
import numpy
import os
import time
# space = [[random.choice(['X','0']) for _ in range(20)] for _ in range(20)]

size = 40
space_size = size**2
living_cell_string = 'X'
dead_cell_string = 'O'

better_space = [random.choice([living_cell_string, dead_cell_string]) for _ in range(size**2)]
better_space = numpy.array(better_space)
better_spacer = '_' * size
def print_da_game(better_space:numpy.array) -> None:
    os.system('cls')
    counter = 1
    for cell in better_space:
        print(cell,end='')
        if counter == size:
            print()
            counter = 0
        counter += 1
    print(better_spacer)

def in_range_checker(cell_index:int) -> bool:
    # print(cell_index)
    if cell_index > size**2 - 1 or cell_index < 0:
        return False
    return True

def count_adjacent_living_cells(space:numpy.array, cell_index:int) -> int:
    cell_pos_modifiers = [cell_index - size - 1, cell_index - size, cell_index - size + 1, cell_index - 1, cell_index + 1, cell_index + size - 1, cell_index + size, cell_index + size + 1]
    number_of_adjacent_living_cells = 0
    for cell_pos_modifier in cell_pos_modifiers:
        if in_range_checker(cell_pos_modifier):
            if space[cell_pos_modifier] == living_cell_string:
                number_of_adjacent_living_cells += 1
    return number_of_adjacent_living_cells

def gen_next_state(better_space_init:numpy.array) -> numpy.array:
    better_space = list(better_space_init)
    for index, cell in enumerate(better_space):
        if count_adjacent_living_cells(better_space, index) == 3 and cell == dead_cell_string:
            cell = living_cell_string
        if (count_adjacent_living_cells(better_space, index) == 2 or count_adjacent_living_cells(better_space, index) == 3) and cell == living_cell_string:
            cell = living_cell_string
        else:
            cell = dead_cell_string
    return numpy.array(better_space)

def play_the_game(iterations:int):
    print_da_game(better_space)
    for iteration in range(iterations):
        if iteration == 0:
            next = gen_next_state(better_space)
        else:
            next = gen_next_state(next)
        time.sleep(0.15)

play_the_game(100)