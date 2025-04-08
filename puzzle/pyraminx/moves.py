import numpy as np
def execute_move(state, move):
    new_state = {}
    new_state["to"] = np.mod(state["to"]+move["to"], 3)
    if "co" in move:
        new_state["co"] = np.mod(state["co"]+move["co"], 3)
    else:
        new_state["co"] = state["co"]
    if "ep" in move:
        new_state["eo"] = move["ep"] @ state["eo"]
        new_state["ep"] = move["ep"] @ state["ep"]
        new_state["eo"] = np.mod(new_state["eo"]+move["eo"], 2)
    else:
        new_state["eo"] = state["eo"]
        new_state["ep"] = state["ep"]
    return new_state
def execute_no_ct(state, move):
    new_state = {}
    new_state["eo"] = move["ep"] @ state["eo"]
    new_state["ep"] = move["ep"] @ state["ep"]
    new_state["eo"] = np.mod(new_state["eo"]+move["eo"], 2)
    return new_state
moves = {
    "I": {
        "co": np.array([0,0,0,0], np.dtype("int8")),
        "to": np.array([0,0,0,0], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0],
                        [0,1,0,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,0,1,0,0],
                        [0,0,0,0,1,0],
                        [0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([0,0,0,0,0,0], np.dtype("int8"))
    },
    "U": {
        "co": np.array([1,0,0,0], np.dtype("int8")),
        "to": np.array([1,0,0,0], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0],
                        [0,1,0,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,0,0,0,1],
                        [0,0,0,1,0,0],
                        [0,0,0,0,1,0]], np.dtype("int8")),
        "eo": np.array([0,0,0,0,0,0], np.dtype("int8"))
    },
    "U'": {
        "co": np.array([2,0,0,0], np.dtype("int8")),
        "to": np.array([2,0,0,0], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0],
                        [0,1,0,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,0,0,1,0],
                        [0,0,0,0,0,1],
                        [0,0,0,1,0,0]], np.dtype("int8")),
        "eo": np.array([0,0,0,0,0,0], np.dtype("int8"))
    },
    "R": {
        "co": np.array([0,1,0,0], np.dtype("int8")),
        "to": np.array([0,1,0,0], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,0,1,0,0],
                        [0,1,0,0,0,0],
                        [0,0,0,0,1,0],
                        [0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([0,0,0,0,0,0], np.dtype("int8"))
    },
    "R'": {
        "co": np.array([0,2,0,0], np.dtype("int8")),
        "to": np.array([0,2,0,0], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0],
                        [0,0,0,1,0,0],
                        [0,1,0,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,0,0,1,0],
                        [0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([0,0,0,0,0,0], np.dtype("int8"))
    },
    "L": {
        "co": np.array([0,0,1,0], np.dtype("int8")),
        "to": np.array([0,0,1,0], np.dtype("int8")),
        "ep": np.array([[0,1,0,0,0,0],
                        [0,0,0,0,1,0],
                        [0,0,1,0,0,0],
                        [0,0,0,1,0,0],
                        [1,0,0,0,0,0],
                        [0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([0,1,0,0,1,0], np.dtype("int8"))
    },
    "L'": {
        "co": np.array([0,0,2,0], np.dtype("int8")),
        "to": np.array([0,0,2,0], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,1,0],
                        [1,0,0,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,0,1,0,0],
                        [0,1,0,0,0,0],
                        [0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([1,0,0,0,1,0], np.dtype("int8"))
    },
    "B": {
        "co": np.array([0,0,0,1], np.dtype("int8")),
        "to": np.array([0,0,0,1], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,1],
                        [0,1,0,0,0,0],
                        [1,0,0,0,0,0],
                        [0,0,0,1,0,0],
                        [0,0,0,0,1,0],
                        [0,0,1,0,0,0]], np.dtype("int8")),
        "eo": np.array([0,0,1,0,0,1], np.dtype("int8"))
    },
    "B'": {
        "co": np.array([0,0,0,2], np.dtype("int8")),
        "to": np.array([0,0,0,2], np.dtype("int8")),
        "ep": np.array([[0,0,1,0,0,0],
                        [0,1,0,0,0,0],
                        [0,0,0,0,0,1],
                        [0,0,0,1,0,0],
                        [0,0,0,0,1,0],
                        [1,0,0,0,0,0]], np.dtype("int8")),
        "eo": np.array([1,0,1,0,0,0], np.dtype("int8"))
    },
    "u": {
        "to": np.array([1,0,0,0], np.dtype("int8"))
    },
    "u'": {
        "to": np.array([2,0,0,0], np.dtype("int8"))
    },
    "r": {
        "to": np.array([0,1,0,0], np.dtype("int8"))
    },
    "r'": {
        "to": np.array([0,2,0,0], np.dtype("int8"))
    },
    "l": {
        "to": np.array([0,0,1,0], np.dtype("int8"))
    },
    "l'": {
        "to": np.array([0,0,2,0], np.dtype("int8"))
    },
    "b": {
        "to": np.array([0,0,0,1], np.dtype("int8")),
    },
    "b'": {
        "to": np.array([0,0,0,2], np.dtype("int8")),
    }
}