import numpy as np
"""
UR UL DR DL
corners odd, edges even
standard order is UBR->UR->...->UBL->UB->DBR->DR->...->DBL->DB
"""
solved_state = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], np.dtype("int8"))
slash_arr = np.array([[0,0,1,0],
                      [0,1,0,0],
                      [1,0,0,0],
                      [0,0,0,1]], np.dtype("int8"))
def execute_move(state, move):
    if type(state) == bool:
        return state
    if move == "/":
        new_state = np.array([state[2], state[1], state[0], state[3]], np.dtype("object"))
        new_state[0] = new_state[0][::-1]
        new_state[2] = new_state[2][::-1]
        return new_state
    else:
        new_state = np.empty((4), np.dtype("object"))
        move = [int(i) for i in move.strip(" ()").split(",")]
        for l in [0,1]:
            if move[l] != 0:
                r_indices = range(len(state[l*2]))
                l_indices = range(len(state[l*2+1]))
                if l == 0:
                    if move[l] > 0:
                        r_indices = reversed(r_indices)
                        l_indices = reversed(l_indices)
                else:
                    if move[l] < 0:
                        r_indices = reversed(r_indices)
                        l_indices = reversed(l_indices)
                r_sum = 0
                r_pieces = []
                l_sum = 0
                l_pieces = []
                for i in r_indices:
                    if state[l*2][i] % 2 == 0:
                        r_sum += 1
                    else:
                        r_sum += 2
                    r_pieces.append(state[l*2][i])
                    if r_sum == abs(move[l]):
                        break
                    elif r_sum > abs(move[l]):
                        return False
                for i in l_indices:
                    if state[l*2+1][i] % 2 == 0:
                        l_sum += 1
                    else:
                        l_sum += 2
                    l_pieces.append(state[l*2+1][i])
                    if l_sum == abs(move[l]):
                        break
                    elif l_sum > abs(move[l]):
                        return False
                # works
                if l == 0:
                    if move[l] > 0:
                        new_state[l*2] = np.concatenate((np.array(l_pieces)[::-1], state[l*2][:-len(r_pieces)]))
                        new_state[l*2+1] = np.concatenate((np.array(r_pieces)[::-1], state[l*2+1][:-len(l_pieces)]))
                    else:
                        new_state[l*2] = np.concatenate((state[l*2][len(r_pieces):], np.array(l_pieces)))
                        new_state[l*2+1] = np.concatenate((state[l*2+1][len(l_pieces):], np.array(r_pieces)))
                else:
                    if move[l] > 0:
                        new_state[l*2] = np.concatenate((state[l*2][len(r_pieces):], np.array(l_pieces)))
                        new_state[l*2+1] = np.concatenate((state[l*2+1][len(l_pieces):], np.array(r_pieces)))
                    else:
                        new_state[l*2] = np.concatenate((np.array(l_pieces)[::-1], state[l*2][:-len(r_pieces)]))
                        new_state[l*2+1] = np.concatenate((np.array(r_pieces)[::-1], state[l*2+1][:-len(l_pieces)]))
            else:
                new_state[l*2] = state[l*2].copy()
                new_state[l*2+1] = state[l*2+1].copy()
        return new_state
def execute_alg(state, alg):
    if alg:
        if type(alg) == str:
            alg = alg.strip().split(" ")
        new_state = state
        for step in alg:
            step = step.strip()
            new_state = execute_move(new_state, step)
        return new_state
    else:
        return state
def get_combined(state):
    return np.concatenate((state[0], state[1], state[2], state[3]))
checker_nums = {
    2: "10",
    4: "11",
    1: "01",
}
def pack_checker(state):
    result = ""
    for i in range(0,4):
        for j in range(0,len(state[i])):
            result += checker_nums[state[i][j]]
    result = int(result, 2)
    return result
def invert_alg(alg):
    if alg:
        alg = alg.split(" ")
        result = []
        for step in reversed(alg):
            if step == "/":
                result.append(step)
            else:
                step = step.strip(" ()").split(",")
                final_step = "("
                if step[0] == "0" or step[0] == "6":
                    final_step += step[0]
                elif step[0][0] == "-":
                    final_step += step[0][1:]
                else:
                    final_step += "-"+step[0]
                final_step += ","
                if step[1] == "0" or step[1] == "6":
                    final_step += step[1]
                elif step[1][0] == "-":
                    final_step += step[1][1:]
                else:
                    final_step += "-"+step[1]
                final_step += ")"
                result.append(final_step)
        return " ".join(result)
    else:
        return alg