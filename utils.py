def download_image(options_str, file_name):
    with open("testimg.html", "w") as f:
        f.write("<!DOCTYPE html>"+"\n")
        f.write("<head>"+"\n")
        f.write("    <script type='text/javascript' src='puzzleGen.min.js'></script>"+"\n")
        f.write("</head>"+"\n")
        f.write("<body>"+"\n")
        f.write("</body>"+"\n")
        f.write("<script>"+"\n")
        f.write("    var options_test = "+options_str+";"+"\n")
        f.write("    puzzleGen.Canvas(document.body, puzzleGen.Type.SQUARE1_NET, options_test);"+"\n")
        f.write("    document.addEventListener('DOMContentLoaded', function(e) {"+"\n")
        f.write("        let testObj = document.getElementsByTagName('canvas')[0];"+"\n")
        f.write("        var a = document.createElement('a');"+"\n")
        f.write("        a.href = testObj.toDataURL('image/png');"+"\n")
        f.write("        a.download = '"+file_name+"';\n")
        f.write("        a.click();"+"\n")
        f.write("    });"+"\n")
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

def read_batchsolver_csv(filepath):
    with open(filepath, "r") as f:
        raw_data = f.readlines()
    # get rid of empty image row
    if raw_data[0].startswith(",,"):
        raw_data = raw_data[1:]
    raw_data = [x.split(",") for x in raw_data]
    primary_sort = raw_data[0][0].strip()
    print(primary_sort)
    raw_data = raw_data[1:]
    secondary_sort = None
    if "[" in raw_data[0][1]:
        secondary_sort = raw_data[0][1][raw_data[0][1].find("[")+1:raw_data[0][1].find("]")].split(" ")[1]
    case_dict = {}
    i = 0
    while i < len(raw_data[0]):
        case_num = i//2+1
        alg_val = float(raw_data[0][i])
        if secondary_sort:
            alg_str = raw_data[0][i+1][:raw_data[0][i+1].find("[")].strip()
            alg_val_2 = float(raw_data[0][i+1][raw_data[0][i+1].find("[")+1:].split(" ")[0])
            case_dict[case_num] = {"alg": alg_str, primary_sort: alg_val, secondary_sort:alg_val_2}
        else:
            alg_str = raw_data[0][i+1]
            case_dict[case_num] = {"alg": alg_str, primary_sort: alg_val}
        i += 2
    for row in raw_data[1:]:
        i = 0
        while i < len(row):
            if row[i]:
                case_num = i//2+1
                alg_val = float(row[i])
                if secondary_sort:
                    alg_str = row[i+1][:row[i+1].find("[")].strip()
                    alg_val_2 = float(row[i+1][row[i+1].find("[")+1:].split(" ")[0])
                    case_dict[case_num] = {"alg": alg_str, primary_sort: alg_val, secondary_sort:alg_val_2}
                else:
                    alg_str = row[i+1]
                    case_dict[case_num] = {"alg": alg_str, primary_sort: alg_val}
            i += 2
    return case_dict