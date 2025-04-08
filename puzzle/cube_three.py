import numpy as np
default_state = {
    "co": np.array([0, 0, 0, 0, 0, 0, 0, 0], np.dtype("int8")),
    "cp": np.array([1, 2, 3, 4, 5, 6, 7, 8], np.dtype("int8")),
    "eo": np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], np.dtype("int8")),
    "ep": np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], np.dtype("int8")),
    "cep": np.array([1, 2, 3, 4, 5, 6], np.dtype("int8"))
}
piece_names = {
    "co": ["DBL", "DLF", "DFR", "DRB", "ULB", "UFL", "URF", "UBR"],
    "cp": ["DBL", "DLF", "DFR", "DRB", "ULB", "UFL", "URF", "UBR"],
    "eo": ["DL", "DF", "DR", "DB", "BL", "FL", "FR", "BR", "UL", "UF", "UR", "UB"],
    "ep": ["DL", "DF", "DR", "DB", "BL", "FL", "FR", "BR", "UL", "UF", "UR", "UB"],
    "cep": ["D", "U", "L", "F", "R", "B"]
}
piece_names_clean = {
    "co": ["DBL", "DFL", "DFR", "DBR", "UBL", "UFL", "UFR", "UBR"],
    "cp": ["DBL", "DFL", "DFR", "DBR", "UBL", "UFL", "UFR", "UBR"],
    "eo": ["DL", "DF", "DR", "DB", "BL", "FL", "FR", "BR", "UL", "UF", "UR", "UB"],
    "ep": ["DL", "DF", "DR", "DB", "BL", "FL", "FR", "BR", "UL", "UF", "UR", "UB"],
    "cep": ["D", "U", "L", "F", "R", "B"]
}
names_to_default_indexes = {
    "DBL": 1, "DLF": 2, "DFR": 3, "DRB": 4, "ULB": 5, "UFL": 6, "URF": 7, "UBR": 8,
    "DL": 1, "DF": 2, "DR": 3, "DB": 4, "BL": 5, "FL": 6, "FR": 7, "BR": 8, "UL": 9, "UF": 10, "UR": 11, "UB": 12,
    "D": 1, "U": 2, "L": 3, "F": 4, "R": 5, "B": 6
}
category_types = {
    "order": ["co", "eo", "cp", "ep", "cep"],
    "co": ("o", 3),
    "cp": ("p", "co"),
    "eo": ("o", 2),
    "ep": ("p", "eo"),
    "cep": ("p")
}

def state_to_puzzlegen(state, masking=None, extra_options=None, extra_puzzle_options=None, color_scheme=None):
    # State to stickerColors for puzzle-gen
    options = {}
    options["puzzle"] = {}
    if not color_scheme:
        # Use default
        color_scheme = {
            "U": "puzzleGen.Colors.YELLOW",
            "F": "puzzleGen.Colors.BLUE",
            "R": "puzzleGen.Colors.RED",
            "D": "puzzleGen.Colors.WHITE",
            "B": "puzzleGen.Colors.GREEN",
            "L": "puzzleGen.Colors.ORANGE"
        }
    if not masking:
        masking = {"corners":[], "edges":[], "centers":[]}
    options["puzzle"]["size"] = 3
    options["puzzle"]["stickerColors"] = {}
    options["puzzle"]["stickerColors"]["U"] = ["puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR"]
    options["puzzle"]["stickerColors"]["F"] = ["puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR"]
    options["puzzle"]["stickerColors"]["R"] = ["puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR"]
    options["puzzle"]["stickerColors"]["D"] = ["puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR"]
    options["puzzle"]["stickerColors"]["B"] = ["puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR"]
    options["puzzle"]["stickerColors"]["L"] = ["puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR", "puzzleGen.Colors.MASK_COLOR"]
    #corners
    i = 0
    while i < len(state["cp"]):
        orientation = state["co"][i]
        orig_corner_name = piece_names["co"][state["cp"][i]-1]
        corner_name = orig_corner_name[-orientation:] + orig_corner_name[:-orientation]
        match i:
            case 0:
                if orig_corner_name+corner_name[0] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["D"][0] = color_scheme[corner_name[0]]
                if orig_corner_name+corner_name[1] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["B"][8] = color_scheme[corner_name[1]]
                if orig_corner_name+corner_name[2] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["L"][6] = color_scheme[corner_name[2]]
            case 1:
                if orig_corner_name+corner_name[0] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["D"][6] = color_scheme[corner_name[0]]
                if orig_corner_name+corner_name[1] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["L"][8] = color_scheme[corner_name[1]]
                if orig_corner_name+corner_name[2] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["F"][6] = color_scheme[corner_name[2]]
            case 2:
                if orig_corner_name+corner_name[0] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["D"][8] = color_scheme[corner_name[0]]
                if orig_corner_name+corner_name[1] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["F"][8] = color_scheme[corner_name[1]]
                if orig_corner_name+corner_name[2] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["R"][6] = color_scheme[corner_name[2]]
            case 3:
                if orig_corner_name+corner_name[0] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["D"][2] = color_scheme[corner_name[0]]
                if orig_corner_name+corner_name[1] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["R"][8] = color_scheme[corner_name[1]]
                if orig_corner_name+corner_name[2] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["B"][6] = color_scheme[corner_name[2]]
            case 4:
                if orig_corner_name+corner_name[0] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["U"][0] = color_scheme[corner_name[0]]
                if orig_corner_name+corner_name[1] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["L"][0] = color_scheme[corner_name[1]]
                if orig_corner_name+corner_name[2] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["B"][2] = color_scheme[corner_name[2]]
            case 5:
                if orig_corner_name+corner_name[0] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["U"][6] = color_scheme[corner_name[0]]
                if orig_corner_name+corner_name[1] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["F"][0] = color_scheme[corner_name[1]]
                if orig_corner_name+corner_name[2] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["L"][2] = color_scheme[corner_name[2]]
            case 6:
                if orig_corner_name+corner_name[0] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["U"][8] = color_scheme[corner_name[0]]
                if orig_corner_name+corner_name[1] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["R"][0] = color_scheme[corner_name[1]]
                if orig_corner_name+corner_name[2] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["F"][2] = color_scheme[corner_name[2]]
            case 7:
                if orig_corner_name+corner_name[0] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["U"][2] = color_scheme[corner_name[0]]
                if orig_corner_name+corner_name[1] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["B"][0] = color_scheme[corner_name[1]]
                if orig_corner_name+corner_name[2] not in masking["corners"]:
                    options["puzzle"]["stickerColors"]["R"][2] = color_scheme[corner_name[2]]
        i += 1
    #centers
    i = 0
    while i < len(state["cep"]):
        center_name = piece_names["cep"][state["cep"][i]-1]
        match i:
            case 0:
                if center_name not in masking["centers"]:
                    options["puzzle"]["stickerColors"]["D"][4] = color_scheme[center_name]
            case 1:
                if center_name not in masking["centers"]:
                    options["puzzle"]["stickerColors"]["U"][4] = color_scheme[center_name]
            case 2:
                if center_name not in masking["centers"]:
                    options["puzzle"]["stickerColors"]["L"][4] = color_scheme[center_name]
            case 3:
                if center_name not in masking["centers"]:
                    options["puzzle"]["stickerColors"]["F"][4] = color_scheme[center_name]
            case 4:
                if center_name not in masking["centers"]:
                    options["puzzle"]["stickerColors"]["R"][4] = color_scheme[center_name]
            case 5:
                if center_name not in masking["centers"]:
                    options["puzzle"]["stickerColors"]["B"][4] = color_scheme[center_name]
        i += 1
    #edges
    i = 0
    while i < len(state["ep"]):
        orientation = state["eo"][i]
        orig_edge_name = piece_names["eo"][state["ep"][i]-1]
        edge_name = orig_edge_name[-orientation:] + orig_edge_name[:-orientation]
        match i:
            case 0:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["D"][3] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["L"][7] = color_scheme[edge_name[1]]
            case 1:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["D"][7] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["F"][7] = color_scheme[edge_name[1]]
            case 2:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["D"][5] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["R"][7] = color_scheme[edge_name[1]]
            case 3:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["D"][1] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["B"][7] = color_scheme[edge_name[1]]
            case 4:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["B"][5] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["L"][3] = color_scheme[edge_name[1]]
            case 5:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["F"][3] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["L"][5] = color_scheme[edge_name[1]]
            case 6:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["F"][5] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["R"][3] = color_scheme[edge_name[1]]
            case 7:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["B"][3] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["R"][5] = color_scheme[edge_name[1]]
            case 8:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["U"][3] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["L"][1] = color_scheme[edge_name[1]]
            case 9:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["U"][7] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["F"][1] = color_scheme[edge_name[1]]
            case 10:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["U"][5] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["R"][1] = color_scheme[edge_name[1]]
            case 11:
                if orig_edge_name+edge_name[0] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["U"][1] = color_scheme[edge_name[0]]
                if orig_edge_name+edge_name[1] not in masking["edges"]:
                    options["puzzle"]["stickerColors"]["B"][1] = color_scheme[edge_name[1]]
        i += 1
    options_str = "{'puzzle': {'size': 3, 'stickerColors': {"
    for face, stickers in options["puzzle"]["stickerColors"].items():
        options_str += "'"+face+"': ["
        options_str += ", ".join(stickers)
        options_str += "], "
    options_str = options_str.rstrip(", ")
    options_str += "}"
    if extra_puzzle_options:
        for key, val in extra_puzzle_options.items():
            options_str += "'"+key+"': "+str(val)+", "
        options_str = options_str.rstrip(", ")
    options_str += "}, "
    if extra_options:
        for key, val in extra_options.items():
            options_str += "'"+key+"': "+str(val)+", "
        options_str = options_str.rstrip(", ")
    options_str += "}"
    return options_str

def execute_move_full(state, move):
    new_state = {}
    if "cp" in move:
        new_state["co"] = move["cp"] @ state["co"]
        new_state["cp"] = move["cp"] @ state["cp"]
    else:
        new_state["co"] = state["co"]
        new_state["cp"] = state["cp"]
    if "co" in move:
        new_state["co"] = np.mod(new_state["co"]+move["co"], 3)
    new_state["eo"] = move["ep"] @ state["eo"]
    new_state["ep"] = move["ep"] @ state["ep"]
    if "eo" in move:
        new_state["eo"] = np.mod(new_state["eo"]+move["eo"], 2)
    if "cep" in move:
        new_state["cep"] = move["cep"] @ state["cep"]
    else:
        new_state["cep"] = state["cep"]
    return new_state
def execute_move_RU(state, move):
    new_state = {}
    if "cp" in move:
        new_state["co"] = move["cp"] @ state["co"]
        new_state["cp"] = move["cp"] @ state["cp"]
    else:
        new_state["co"] = state["co"]
        new_state["cp"] = state["cp"]
    if "co" in move:
        new_state["co"] = np.mod(new_state["co"]+move["co"], 3)
    new_state["ep"] = move["ep"] @ state["ep"]
    return new_state

identity = np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
moves = {
    "U": {
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0]], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0]], np.dtype("int8"))
    },
    "U2": {
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0]], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0]], np.dtype("int8"))
    },
    "U'": {
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0]], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0]], np.dtype("int8"))
    },
    "R": {
        "co": np.array([0,0,1,2,0,0,2,1], np.dtype("int8")),
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0]], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "R2": {
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,1,0,0,0,0,0]], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "R'": {
        "co": np.array([0,0,1,2,0,0,2,1], np.dtype("int8")),
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,1,0,0,0,0]], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "L": {
        "co": np.array([1,2,0,0,2,1,0,0], np.dtype("int8")),
        "cp": np.array([[0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "L2": {
        "cp": np.array([[0,0,0,0,0,1,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "L'": {
        "co": np.array([1,2,0,0,2,1,0,0], np.dtype("int8")),
        "cp": np.array([[0,0,0,0,1,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "D": {
        "cp": np.array([[0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "ep": np.array([[0,0,0,1,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "D2": {
        "cp": np.array([[0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "ep": np.array([[0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "D'": {
        "cp": np.array([[0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "ep": np.array([[0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "F": {
        "co": np.array([0,1,2,0,0,2,1,0], np.dtype("int8")),
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([0,1,0,0,0,1,1,0,0,1,0,0], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "F2": {
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "F'": {
        "co": np.array([0,1,2,0,0,2,1,0], np.dtype("int8")),
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([0,1,0,0,0,1,1,0,0,1,0,0], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8"))
    },
    "B": {
        "co": np.array([2,0,0,1,1,0,0,2], np.dtype("int8")),
        "cp": np.array([[0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,1,0,0,0,0]], np.dtype("int8")),
        "eo": np.array([0,0,0,1,1,0,0,1,0,0,0,1], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0]], np.dtype("int8"))
    },
    "B2": {
        "cp": np.array([[0,0,0,0,0,0,0,1],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [1,0,0,0,0,0,0,0]], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0]], np.dtype("int8"))
    },
    "B'": {
        "co": np.array([2,0,0,1,1,0,0,2], np.dtype("int8")),
        "cp": np.array([[0,0,0,1,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,1,0,0,0]], np.dtype("int8")),
        "eo": np.array([0,0,0,1,1,0,0,1,0,0,0,1], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0]], np.dtype("int8"))
    },
    "M": {
        "eo": np.array([0,1,0,1,0,0,0,0,0,1,0,1], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,0,1,0,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,1,0],
                         [1,0,0,0,0,0]], np.dtype("int8"))
    },
    "M2": {
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,1,0,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,1,0,0,0],
                         [0,0,0,0,0,1],
                         [0,0,0,0,1,0],
                         [0,0,0,1,0,0]], np.dtype("int8"))
    },
    "M'": {
        "eo": np.array([0,1,0,1,0,0,0,0,0,1,0,1], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,0,0,0,1],
                         [0,0,0,1,0,0],
                         [0,0,1,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,1,0,0,0,0]], np.dtype("int8"))
    },
    "S": {
        "eo": np.array([1,0,1,0,0,0,0,0,1,0,1,0], np.dtype("int8")),
        "ep": np.array([[0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[0,0,0,0,1,0],
                         [0,0,1,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,1,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,0,1],], np.dtype("int8"))
    },
    "S2": {
        "ep": np.array([[0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[0,1,0,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,1,0,0],
                         [0,0,1,0,0,0],
                         [0,0,0,0,0,1]], np.dtype("int8"))
    },
    "S'": {
        "eo": np.array([1,0,1,0,0,0,0,0,1,0,1,0], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[0,0,1,0,0,0],
                         [0,0,0,0,1,0],
                         [0,1,0,0,0,0],
                         [0,0,0,1,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,0,1]], np.dtype("int8"))
    },
    "E": {
        "eo": np.array([0,0,0,0,1,1,1,1,0,0,0,0], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,0,0,1,0,0],
                         [0,0,0,0,1,0],], np.dtype("int8"))
    },
    "E2": {
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,0,0,1,0,0]], np.dtype("int8"))
    },
    "E'": {
        "eo": np.array([0,0,0,0,1,1,1,1,0,0,0,0], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,1,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0]], np.dtype("int8"))
    },
    "u": {
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0]], np.dtype("int8")),
        "eo": np.array([0,0,0,0,1,1,1,1,0,0,0,0], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,1,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0]], np.dtype("int8"))
    },
    "u2": {
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0]], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,0,0,1,0,0]], np.dtype("int8"))
    },
    "u'": {
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0]], np.dtype("int8")),
        "eo": np.array([0,0,0,0,1,1,1,1,0,0,0,0], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,0,0,1,0,0],
                         [0,0,0,0,1,0],], np.dtype("int8"))
    },
    "r": {
        "co": np.array([0,0,1,2,0,0,2,1], np.dtype("int8")),
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0]], np.dtype("int8")),
        "eo": np.array([0,1,0,1,0,0,0,0,0,1,0,1], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,0,0,0,1],
                         [0,0,0,1,0,0],
                         [0,0,1,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,1,0,0,0,0]], np.dtype("int8"))
    },
    "r2": {
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,1,0,0,0,0,0]], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,1,0,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,1,0,0,0],
                         [0,0,0,0,0,1],
                         [0,0,0,0,1,0],
                         [0,0,0,1,0,0]], np.dtype("int8"))
    },
    "r'": {
        "co": np.array([0,0,1,2,0,0,2,1], np.dtype("int8")),
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,1,0,0,0,0]], np.dtype("int8")),
        "eo": np.array([0,1,0,1,0,0,0,0,0,1,0,1], np.dtype("int8")),
        "ep": np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,0,1,0,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,1,0],
                         [1,0,0,0,0,0]], np.dtype("int8"))
    },
    "l": {
        "co": np.array([1,2,0,0,2,1,0,0], np.dtype("int8")),
        "cp": np.array([[0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([0,1,0,1,0,0,0,0,0,1,0,1], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,0,1,0,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,1,0],
                         [1,0,0,0,0,0]], np.dtype("int8"))
    },
    "l2": {
        "cp": np.array([[0,0,0,0,0,1,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,1,0,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,1,0,0,0],
                         [0,0,0,0,0,1],
                         [0,0,0,0,1,0],
                         [0,0,0,1,0,0]], np.dtype("int8"))
    },
    "l'": {
        "co": np.array([1,2,0,0,2,1,0,0], np.dtype("int8")),
        "cp": np.array([[0,0,0,0,1,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([0,1,0,1,0,0,0,0,0,1,0,1], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,0,0,0,1],
                         [0,0,0,1,0,0],
                         [0,0,1,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,1,0,0,0,0]], np.dtype("int8"))
    },
    "d": {
        "cp": np.array([[0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([0,0,0,0,1,1,1,1,0,0,0,0], np.dtype("int8")),
        "ep": np.array([[0,0,0,1,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,0,0,1,0,0],
                         [0,0,0,0,1,0],], np.dtype("int8"))
    },
    "d2": {
        "cp": np.array([[0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "ep": np.array([[0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,0,0,1,0,0]], np.dtype("int8"))
    },
    "d'": {
        "cp": np.array([[0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([0,0,0,0,1,1,1,1,0,0,0,0], np.dtype("int8")),
        "ep": np.array([[0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,1,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0]], np.dtype("int8"))
    },
    "f": {
        "co": np.array([0,1,2,0,0,2,1,0], np.dtype("int8")),
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([1,0,1,0,0,0,0,0,1,0,1,0], np.dtype("int8")),
        "ep": np.array([[0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[0,0,0,0,1,0],
                         [0,0,1,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,1,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,0,1],], np.dtype("int8"))
    },
    "f2": {
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[0,1,0,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,1,0,0],
                         [0,0,1,0,0,0],
                         [0,0,0,0,0,1]], np.dtype("int8"))
    },
    "f'": {
        "co": np.array([0,1,2,0,0,2,1,0], np.dtype("int8")),
        "cp": np.array([[1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "eo": np.array([1,0,1,0,0,0,0,0,1,0,1,0], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]], np.dtype("int8")),
        "cep": np.array([[0,0,1,0,0,0],
                         [0,0,0,0,1,0],
                         [0,1,0,0,0,0],
                         [0,0,0,1,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,0,1]], np.dtype("int8"))
    },
    "b": {
        "co": np.array([2,0,0,1,1,0,0,2], np.dtype("int8")),
        "cp": np.array([[0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,1,0,0,0,0]], np.dtype("int8")),
        "eo": np.array([1,0,1,0,0,0,0,0,1,0,1,0], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,1,0,0,0],
                         [0,0,0,0,1,0],
                         [0,1,0,0,0,0],
                         [0,0,0,1,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,0,1]], np.dtype("int8"))
    },
    "b2": {
        "cp": np.array([[0,0,0,0,0,0,0,1],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [1,0,0,0,0,0,0,0]], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,1,0,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,1,0,0],
                         [0,0,1,0,0,0],
                         [0,0,0,0,0,1]], np.dtype("int8"))
    },
    "b'": {
        "co": np.array([2,0,0,1,1,0,0,2], np.dtype("int8")),
        "cp": np.array([[0,0,0,1,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,1,0,0,0]], np.dtype("int8")),
        "eo": np.array([1,0,1,0,0,0,0,0,1,0,1,0], np.dtype("int8")),
        "ep": np.array([[0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,0,0,1,0],
                         [0,0,1,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,1,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,0,1],], np.dtype("int8"))
    },
    "x": {
        "co": np.array([1,2,1,2,2,1,2,1], np.dtype("int8")),
        "cp": np.array([[0,0,0,0,1,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,1,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0]], np.dtype("int8")),
        "eo": np.array([0,1,0,1,0,0,0,0,0,1,0,1], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,0,0,0,1],
                         [0,0,0,1,0,0],
                         [0,0,1,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,1,0,0,0,0]], np.dtype("int8"))
    },
    "x2": {
        "cp": np.array([[0,0,0,0,0,1,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,1,0],
                        [0,1,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,1,0,0,0,0,0]], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,1,0,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,1,0,0,0],
                         [0,0,0,0,0,1],
                         [0,0,0,0,1,0],
                         [0,0,0,1,0,0]], np.dtype("int8"))
    },
    "x'": {
        "co": np.array([1,2,1,2,2,1,2,1], np.dtype("int8")),
        "cp": np.array([[0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,1,0,0,0,0]], np.dtype("int8")),
        "eo": np.array([0,1,0,1,0,0,0,0,0,1,0,1], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,0,1,0,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,1,0],
                         [1,0,0,0,0,0]], np.dtype("int8"))
    },
    "y": {
        "cp": np.array([[0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0]], np.dtype("int8")),
        "eo": np.array([0,0,0,0,1,1,1,1,0,0,0,0], np.dtype("int8")),
        "ep": np.array([[0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,1,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0]], np.dtype("int8"))
    },
    "y2": {
        "cp": np.array([[0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0]], np.dtype("int8")),
        "ep": np.array([[0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,0,0,1,0,0]], np.dtype("int8"))
    },
    "y'": {
        "cp": np.array([[0,0,0,1,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,1,0]], np.dtype("int8")),
        "eo": np.array([0,0,0,0,1,1,1,1,0,0,0,0], np.dtype("int8")),
        "ep": np.array([[0,0,0,1,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0]], np.dtype("int8")),
        "cep": np.array([[1,0,0,0,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,0],
                         [0,0,0,1,0,0],
                         [0,0,0,0,1,0],], np.dtype("int8"))
    },
    "z": {
        "co": np.array([2,1,2,1,1,2,1,2], np.dtype("int8")),
        "cp": np.array([[0,0,0,1,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,1,0,0,0]], np.dtype("int8")),
        "eo": np.array([1,1,1,1,1,1,1,1,1,1,1,1], np.dtype("int8")),
        "ep": np.array([[0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,0,0,1,0],
                         [0,0,1,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,1,0,0],
                         [0,1,0,0,0,0],
                         [0,0,0,0,0,1],], np.dtype("int8"))
    },
    "z2": {
        "cp": np.array([[0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0]], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,1,0,0,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,1,0],
                         [0,0,0,1,0,0],
                         [0,0,1,0,0,0],
                         [0,0,0,0,0,1]], np.dtype("int8"))
    },
    "z'": {
        "co": np.array([2,1,2,1,1,2,1,2], np.dtype("int8")),
        "cp": np.array([[0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,1,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0]], np.dtype("int8")),
        "eo": np.array([1,1,1,1,1,1,1,1,1,1,1,1], np.dtype("int8")),
        "ep": np.array([[0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0]], np.dtype("int8")),
        "cep": np.array([[0,0,1,0,0,0],
                         [0,0,0,0,1,0],
                         [0,1,0,0,0,0],
                         [0,0,0,1,0,0],
                         [1,0,0,0,0,0],
                         [0,0,0,0,0,1]], np.dtype("int8"))
    }
}