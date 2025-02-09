class Tree:
    def __init__(self, state, last_move, parent=None, children=None, is_solved=False):
        self.last_move = last_move
        self.state = state
        self.children = children or []
        self.parent = parent
        self.is_solved = is_solved

    def add_child(self, state, performed_move):
        new_child = Tree(state, last_move=performed_move, parent=self)
        self.children.append(new_child)
        return new_child
    
    def is_root(self):
        return self.parent is None
    
    def is_leaf(self):
        return not self.children
    
    def get_all_children_states(self):
        all_states = []
        for child in self.children:
            all_states.append(child.state)
            all_states += child.get_all_children_states()
        return all_states
    
    def get_scramble_alg(self):
        #print(self.state)
        if not self.is_root():
            return self.parent.get_scramble_alg().strip(" -")+" "+self.last_move.strip(" -")
        return ""
    
    def get_solving_alg(self):
        #print(self.state)
        if not self.is_root():
            return self.get_inverted_move().strip(" -")+" "+self.parent.get_solving_alg().strip(" -")
        return ""

    def get_inverted_move(self):
        if "2" in self.last_move or "-" in self.last_move:
            return self.last_move
        elif "'" in self.last_move:
            return self.last_move.replace("'", "")
        return self.last_move+"'"
    
    def get_all_leaves(self):
        if self.is_leaf():
            return [self]
        else:
            return_list = []
            for child in self.children:
                return_list += child.get_all_leaves()
            return return_list