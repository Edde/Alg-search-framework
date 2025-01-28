class Tree:
    def __init__(self, state, last_move, parent=None, children=None):
        self.last_move = last_move
        self.state = state
        self.children = children or []
        self.parent = parent

    def add_child(self, state):
        new_child = Tree(state, parent=self)
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
    
    def get_entire_alg(self):
        return self.parent.get_entire_alg()+" "+self.last_move