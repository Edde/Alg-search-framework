import numpy as np
default_state = {
    "co": np.array([0, 0, 0, 0, 0, 0, 0, 0], np.dtype("int8")),
    "cp": np.array([1, 2, 3, 4, 5, 6, 7, 8], np.dtype("int8"))
}
category_names = {
    "co": "Corner orientation",
    "cp": "Corner permutation"
}
piece_names = {
    "co": ["DBL", "DLF", "DFR", "DRB", "ULB", "UFL", "URF", "UBR"],
    "cp": ["DBL", "DLF", "DFR", "DRB", "ULB", "UFL", "URF", "UBR"]
}
names_to_default_indexes = {
    "DBL": 1, "DLF": 2, "DFR": 3, "DRB": 4, "ULB": 5, "UFL": 6, "URF": 7, "UBR": 8
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