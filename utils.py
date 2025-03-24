def create_test_html(options_str, file_name):
    with open(file_name, "w") as f:
        f.write("<!DOCTYPE html>"+"\n")
        f.write("<head>"+"\n")
        f.write("    <title>Visualizer</title>"+"\n")
        f.write("    <script type='text/javascript' src='puzzleGen.min.js'></script>"+"\n")
        f.write("    <script srt='jquery-3.7.1.min.js'></script>"+"\n")
        f.write("</head>"+"\n")
        f.write("<body>"+"\n")
        f.write("</body>"+"\n")
        f.write("<script>"+"\n")
        f.write("    var options_test = "+options_str+";"+"\n")
        f.write("    puzzleGen.PNG(document.body, puzzleGen.Type.CUBE, options_test);"+"\n")
        f.write("</script>"+"\n")

def get_alg_length(alg_str, ignore_pre=False, cancel_moves = True):
    if alg_str:
        if cancel_moves:
            reduced = False
            chars = "".join(set(alg_str))
            chars = chars.replace("'", "").replace("2", "").replace(" ", "")
            while not reduced:
                pre_len = len(alg_str)
                i = 0
                while i < len(chars):
                    alg_str = alg_str.replace(" "+chars[i]+" "+chars[i]+"'", "")
                    alg_str = alg_str.replace(chars[i]+" "+chars[i]+"' ", "")
                    alg_str = alg_str.replace(" "+chars[i]+"' "+chars[i], "")
                    alg_str = alg_str.replace(chars[i]+"' "+chars[i]+" ", "")
                    alg_str = alg_str.replace(" "+chars[i]+"2 "+chars[i]+"2", "")
                    alg_str = alg_str.replace(chars[i]+"2 "+chars[i]+"2 ", "")
                    i += 1
                if pre_len == len(alg_str):
                    reduced = True
        alg_str = alg_str.strip()
        pre_adjust = 1 if ignore_pre else 0
        return (len(alg_str.split(" "))-alg_str.count("(")+pre_adjust)
    else:
        return 0

def execute_alg(state, alg, move_func, moves):
    if alg:
        alg = alg.split(" ")
        new_state = state
        for step in alg:
            step = step.strip("()")
            step = step.strip("*1")
            new_state = move_func(new_state, moves[step])
        return new_state
    else:
        return state

def execute_invert(state, alg, move_func, moves):
    if alg:
        invert_alg = get_invert_of_alg(alg)
        new_state = execute_alg(state, invert_alg, move_func, moves)
        return new_state
    else:
        return state

def get_invert_of_alg(alg_str):
    invert_alg = ""
    if alg_str:
        alg = alg_str.split(" ")
        for step in alg[::-1]:
            step = step.strip("()")
            if "'" in step:
                step = step.replace("'", "")
            elif "2" not in step:
                step = step+"'"
            invert_alg += step+" "
        invert_alg = invert_alg.strip()
    return invert_alg

def comp_states(state1, state2):
    states_same = True
    for k in state1.keys():
        if not (state1[k] == state2[k]).all():
            states_same = False
            break
    return states_same