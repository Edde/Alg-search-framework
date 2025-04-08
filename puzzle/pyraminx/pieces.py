import numpy as np
default_state = {
    "co": np.array([0, 0, 0, 0], np.dtype("int8")),
    "to": np.array([0, 0, 0, 0], np.dtype("int8")),
    "eo": np.array([0, 0, 0, 0, 0, 0], np.dtype("int8")),
    "ep": np.array([1, 2, 3, 4, 5, 6], np.dtype("int8"))
}
piece_names = {
    "co": ["CU", "CR", "CL", "CB"],
    "to": ["TU", "TR", "TL", "TB"],
    "eo": ["DL", "DF", "DR", "UR", "UL", "UB"],
    "ep": ["DL", "DF", "DR", "UR", "UL", "UB"]
}