import numpy as np
default_state = {
    "co": np.array([0, 0, 0, 0, 0, 0, 0, 0], np.dtype("int8")),
    "cp": np.array([0, 1, 2, 3, 4, 5, 6, 7], np.dtype("int8")),
    "eo": np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], np.dtype("int8")),
    "ep": np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], np.dtype("int8")),
    "cep": np.array([0, 1, 2, 3, 4, 5], np.dtype("int8"))
}
category_names = {
    "co": "Corner orientation",
    "cp": "Corner permutation",
    "eo": "Edge orientation",
    "ep": "Edge permutation",
    "cep": "Center permutation",
}
piece_names = {
    "co": ["DBL", "DLF", "DFR", "DRB", "ULB", "UFL", "URF", "UBR"],
    "cp": ["DBL", "DLF", "DFR", "DRB", "ULB", "UFL", "URF", "UBR"],
    "eo": ["DL", "DF", "DR", "DB", "BL", "FL", "FR", "BR", "UL", "UF", "UR", "UB"],
    "ep": ["DL", "DF", "DR", "DB", "BL", "FL", "FR", "BR", "UL", "UF", "UR", "UB"],
    "cep": ["D", "U", "L", "F", "R", "B"]
}
names_to_default_indexes = {
    "DBL": 0, "DLF": 1, "DFR": 2, "DRB": 3, "ULB": 4, "UFL": 5, "URF": 6, "UBR": 7,
    "DL": 0, "DF": 1, "DR": 2, "DB": 3, "LB": 4, "LF": 5, "RF": 6, "RB": 7, "UL": 8, "UF": 9, "UR": 10, "UB": 11,
    "D": 0, "U": 1, "L": 2, "F": 3, "R": 4, "B": 5
}
category_types = {
    "order": ["co", "eo", "cp", "ep", "cep"],
    "co": ("o", 3),
    "cp": ("p", "co"),
    "eo": ("o", 2),
    "ep": ("p", "eo"),
    "cep": ("p")
}

def state_to_puzzlegen(state, piece_names, extra_options=None, extra_puzzle_options=None, color_scheme=None):
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
        corner_name = piece_names["co"][state["cp"][i]]
        corner_name = corner_name[-orientation:] + corner_name[:-orientation]
        match i:
            case 0:
                options["puzzle"]["stickerColors"]["D"][0] = color_scheme[corner_name[0]]
                options["puzzle"]["stickerColors"]["B"][8] = color_scheme[corner_name[1]]
                options["puzzle"]["stickerColors"]["L"][6] = color_scheme[corner_name[2]]
            case 1:
                options["puzzle"]["stickerColors"]["D"][6] = color_scheme[corner_name[0]]
                options["puzzle"]["stickerColors"]["L"][8] = color_scheme[corner_name[1]]
                options["puzzle"]["stickerColors"]["F"][6] = color_scheme[corner_name[2]]
            case 2:
                options["puzzle"]["stickerColors"]["D"][8] = color_scheme[corner_name[0]]
                options["puzzle"]["stickerColors"]["F"][8] = color_scheme[corner_name[1]]
                options["puzzle"]["stickerColors"]["R"][6] = color_scheme[corner_name[2]]
            case 3:
                options["puzzle"]["stickerColors"]["D"][2] = color_scheme[corner_name[0]]
                options["puzzle"]["stickerColors"]["R"][8] = color_scheme[corner_name[1]]
                options["puzzle"]["stickerColors"]["B"][6] = color_scheme[corner_name[2]]
            case 4:
                options["puzzle"]["stickerColors"]["U"][0] = color_scheme[corner_name[0]]
                options["puzzle"]["stickerColors"]["L"][0] = color_scheme[corner_name[1]]
                options["puzzle"]["stickerColors"]["B"][2] = color_scheme[corner_name[2]]
            case 5:
                options["puzzle"]["stickerColors"]["U"][6] = color_scheme[corner_name[0]]
                options["puzzle"]["stickerColors"]["F"][0] = color_scheme[corner_name[1]]
                options["puzzle"]["stickerColors"]["L"][2] = color_scheme[corner_name[2]]
            case 6:
                options["puzzle"]["stickerColors"]["U"][8] = color_scheme[corner_name[0]]
                options["puzzle"]["stickerColors"]["R"][0] = color_scheme[corner_name[1]]
                options["puzzle"]["stickerColors"]["F"][2] = color_scheme[corner_name[2]]
            case 7:
                options["puzzle"]["stickerColors"]["U"][2] = color_scheme[corner_name[0]]
                options["puzzle"]["stickerColors"]["B"][0] = color_scheme[corner_name[1]]
                options["puzzle"]["stickerColors"]["R"][2] = color_scheme[corner_name[2]]
        i += 1
    #centers
    i = 0
    while i < len(state["cep"]):
        center_name = piece_names["cep"][state["cep"][i]]
        match i:
            case 0:
                options["puzzle"]["stickerColors"]["D"][4] = color_scheme[center_name]
            case 1:
                options["puzzle"]["stickerColors"]["U"][4] = color_scheme[center_name]
            case 2:
                options["puzzle"]["stickerColors"]["L"][4] = color_scheme[center_name]
            case 3:
                options["puzzle"]["stickerColors"]["F"][4] = color_scheme[center_name]
            case 4:
                options["puzzle"]["stickerColors"]["R"][4] = color_scheme[center_name]
            case 5:
                options["puzzle"]["stickerColors"]["B"][4] = color_scheme[center_name]
        i += 1
    #edges
    i = 0
    while i < len(state["ep"]):
        orientation = state["eo"][i]
        edge_name = piece_names["eo"][state["ep"][i]]
        edge_name = edge_name[-orientation:] + edge_name[:-orientation]
        match i:
            case 0:
                options["puzzle"]["stickerColors"]["D"][3] = color_scheme[edge_name[0]]
                options["puzzle"]["stickerColors"]["L"][7] = color_scheme[edge_name[1]]
            case 1:
                options["puzzle"]["stickerColors"]["D"][7] = color_scheme[edge_name[0]]
                options["puzzle"]["stickerColors"]["F"][7] = color_scheme[edge_name[1]]
            case 2:
                options["puzzle"]["stickerColors"]["D"][5] = color_scheme[edge_name[0]]
                options["puzzle"]["stickerColors"]["R"][7] = color_scheme[edge_name[1]]
            case 3:
                options["puzzle"]["stickerColors"]["D"][1] = color_scheme[edge_name[0]]
                options["puzzle"]["stickerColors"]["B"][7] = color_scheme[edge_name[1]]
            case 4:
                options["puzzle"]["stickerColors"]["B"][5] = color_scheme[edge_name[0]]
                options["puzzle"]["stickerColors"]["L"][3] = color_scheme[edge_name[1]]
            case 5:
                options["puzzle"]["stickerColors"]["F"][3] = color_scheme[edge_name[0]]
                options["puzzle"]["stickerColors"]["L"][5] = color_scheme[edge_name[1]]
            case 6:
                options["puzzle"]["stickerColors"]["F"][5] = color_scheme[edge_name[0]]
                options["puzzle"]["stickerColors"]["R"][3] = color_scheme[edge_name[1]]
            case 7:
                options["puzzle"]["stickerColors"]["B"][3] = color_scheme[edge_name[0]]
                options["puzzle"]["stickerColors"]["R"][5] = color_scheme[edge_name[1]]
            case 8:
                options["puzzle"]["stickerColors"]["U"][3] = color_scheme[edge_name[0]]
                options["puzzle"]["stickerColors"]["L"][1] = color_scheme[edge_name[1]]
            case 9:
                options["puzzle"]["stickerColors"]["U"][7] = color_scheme[edge_name[0]]
                options["puzzle"]["stickerColors"]["F"][1] = color_scheme[edge_name[1]]
            case 10:
                options["puzzle"]["stickerColors"]["U"][5] = color_scheme[edge_name[0]]
                options["puzzle"]["stickerColors"]["R"][1] = color_scheme[edge_name[1]]
            case 11:
                options["puzzle"]["stickerColors"]["U"][1] = color_scheme[edge_name[0]]
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