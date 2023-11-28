import streamlit as st
import life_game as lg
import time
import numpy

better_space = lg.better_space

def play_the_game(iterations:int):
    global better_space
    not_next = better_space.copy()
    life_container = st.empty()
    iteration_container = st.empty()

    for iteration in range(iterations):
        grid = numpy.reshape(not_next, (lg.size, lg.size))
        st.text(f"Game of Life - Iteration {iteration}")
        display_grid(life_container, grid)
        iteration_container.text(f"Iteration {iteration}")
        not_next = lg.gen_next_state(not_next)
        time.sleep(0.15)

def display_grid(container, grid):
    # container.title(f"Game of Life - Iteration {iterations}")
    html_grid = generate_html_grid(grid)
    container.markdown(html_grid, unsafe_allow_html=True)

def generate_html_grid(grid):
    html = '<div style="display: grid; grid-template-columns: repeat({0}, 20px);">'.format(len(grid[0]))

    for row in grid:
        for value in row:
            color = 'black' if value == lg.living_cell_string else 'white'
            html += '<div style="width: 20px; height: 20px; background-color: {0};"></div>'.format(color)

    html += '</div>'
    return html

st.title("Game of life")
st.write("This is a game of life implementation in python")

iterations = st.slider("Number of iterations", 0, 1000, 100)

if st.button("Run"):
    play_the_game(iterations)
