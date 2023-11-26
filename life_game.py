
import random
import numpy
space = [[random.choice(['X','0']) for _ in range(20)] for _ in range(20)]
size = 20
space_size = size**2

better_space = [random.choice(['X','O']) for _ in range(size**2)]
better_space = numpy.array(better_space)
def print_da_game(better_space:numpy.array) -> None:
    counter = 1
    for cell in better_space:
        print(cell,end='')
        if counter == size:
            print()
            counter = 0
        counter += 1

def in_range_checker(cell_index:int) -> bool:
    if cell_index > size**2:
        return False
    return True

def gen_next_state(better_space:numpy.array):
    better_space = list(better_space)
    for index, cell in enumerate(better_space):
        
