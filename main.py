import numpy as np
from gen_instance.cube_three.SL5C import *
from puzzle_definitions.cube_three.moves import *
from puzzle_definitions.cube_three.pieces import *
from utils import create_test_html
def execute_move(state, move):
    new_state = {}
    for part in category_types["order"]:
        if part in move:
            if category_types[part][0] == "o":
                new_state[part] = np.mod(state[part]+move[part], category_types[part][1])
            elif category_types[part][0] == "p":
                new_state[part] = move[part] @ state[part]
                if len(category_types[part]) == 2:
                    new_state[category_types[part][1]] = move[part] @ new_state[category_types[part][1]]
        else:
            new_state[part] = state[part]
    return new_state
def execute_alg(state, alg):
    alg = alg.split(" ")
    new_state = state
    for step in alg:
        new_state = execute_move(new_state, moves[step])
    return new_state

new_state = execute_alg(default_state, "M' E2 M E2")

#print(new_state)

search_depth = 3
prune_depth = 3

solved_tree = []
extra_options = {"width": 300, "height": 300}

visual_options = state_to_puzzlegen(new_state, piece_names, extra_options=extra_options)

create_test_html(visual_options)