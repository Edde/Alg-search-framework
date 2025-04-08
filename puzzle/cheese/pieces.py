import numpy as np
solved_state = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], np.dtype("int8"))
def check_if_solved_state_alg(alg_str):
    alg_split = alg_str.split(" ")
    if len(alg_split) == 1:
        return True
    elif len(alg_split) == 2 and alg_split[-1] == "S":
        return True
    else:
        for move in alg_split[:-1]:
            if move not in ["U3", "D3", "S"]:
                return False
        return True
category_names = {
    "cp": "Corner permutation",
}
piece_names = {
    "cp": ["DBL", "DL", "DFL", "DFR", "DR", "DBR", "UBR", "UR", "UFR", "UFL", "UL", "UBL"]
}
piece_names_clean = {
    "cp": ["DBL", "DL", "DFL", "DFR", "DR", "DBR", "UBR", "UR", "UFR", "UFL", "UL", "UBL"]
}
names_to_default_indexes = {
    "DBL":1, "DL":2, "DFL":3, "DFR":4, "DR":5, "DBR":6, "UBR":7, "UR":8, "UFR":9, "UFL":10, "UL":11, "UBL":12
}