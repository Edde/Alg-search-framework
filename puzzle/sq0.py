import numpy as np
"""
UBR UFR UFL UBL DBL DFL DFR DBR
"""
moves = {
    "I": np.array([[1,0,0,0,0,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,1,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,0,0,0,0,0,1]], np.dtype("int8")),
    "/": np.array([[0,0,0,0,0,0,1,0],
                    [0,0,0,0,0,0,0,1],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,1,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [1,0,0,0,0,0,0,0],
                    [0,1,0,0,0,0,0,0]], np.dtype("int8")),
    "U": np.array([[0,0,0,1,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,0,1,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,0,0,0,0,0,1]], np.dtype("int8")),
    "U'": np.array([[0,1,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [0,0,0,0,1,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,0,0,0,0,0,1]], np.dtype("int8")),
    "U2": np.array([[0,0,1,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,0,0,1,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,0,0,0,0,0,1]], np.dtype("int8")),
    "D": np.array([[1,0,0,0,0,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,0,1],
                    [0,0,0,0,1,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,1,0]], np.dtype("int8")),
    "D'": np.array([[1,0,0,0,0,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,0,0,0,0,0,1],
                    [0,0,0,0,1,0,0,0]], np.dtype("int8")),
    "D2": np.array([[1,0,0,0,0,0,0,0],
                    [0,1,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,0,0,0,0,0,1],
                    [0,0,0,0,1,0,0,0],
                    [0,0,0,0,0,1,0,0]], np.dtype("int8"))
}
def execute_alg(state, alg):
    if alg:
        if type(alg) == str:
            alg = alg.split(" ")
        new_state = state
        for step in alg:
            step = step.strip()
            new_state = moves[step] @ new_state
        return new_state
    else:
        return state

def execute_move(state, move_str):
    return moves[move_str] @ state

num_to_bin = {
    1: "000",
    2: "001",
    3: "010",
    4: "011",
    5: "100",
    6: "101",
    7: "110",
    8: "111"
}
def get_packed(state):
    return int("".join([num_to_bin[i] for i in state]), 2)
def invert_alg(alg):
    if alg:
        return_str = False
        if type(alg) == str:
            alg = alg.split(" ")
            return_str = True
        inverted_alg = []
        for step in reversed(alg):
            if step.endswith("'"):
                inverted_alg.append(step[0])
            elif step.endswith("2") or step == "/":
                inverted_alg.append(step)
            else:
                inverted_alg.append(step+"'")
        if return_str:
            return " ".join(inverted_alg)
        else:
            return inverted_alg
    else:
        return alg

solved_state = np.array([1, 2, 3, 4, 5, 6, 7, 8], np.dtype("int8"))

U_turns = ["U", "U'", "U2"]
D_turns = ["D", "D'", "D2"]
all_aufs = [["U"], ["U'"], ["U2"], ["D"], ["D'"], ["D2"], ["U","D"], ["U","D'"], ["U","D2"], ["U'","D"], ["U'","D'"], ["U'","D2"], ["U2","D"], ["U2","D'"], ["U2","D2"]]
good_aufs = [["U"], ["U'"], ["D"], ["D'"], ["U","D"], ["U","D'"], ["U'","D"], ["U'","D'"]]
def generate_seq(seq_len, pre_auf, post_auf, used_aufs):
    if seq_len == 1:
        if pre_auf:
            yield ["/"]
            if post_auf:
                for move2 in used_aufs:
                    yield ["/"]+move2
            for move1 in used_aufs:
                if post_auf:
                    yield move1+["/"]
                    for move2 in used_aufs:
                        yield move1+["/"]+move2
                else:
                    yield move1+["/"]
        else:
            yield ["/"]
            for move2 in used_aufs:
                yield ["/"]+move2
    else:
        for seq in generate_seq(seq_len-1, pre_auf, post_auf, used_aufs):
            if post_auf:
                yield seq+["/"]
                for move2 in used_aufs:
                    yield seq+["/"]+move2
            else:
                for move1 in used_aufs:
                    yield seq+move1+["/"]