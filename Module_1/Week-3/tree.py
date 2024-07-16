from graphviz import Graph

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def print_tree(self):
        space = " " + self.get_level() * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.pr int_tree()

class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self) -> int:
        """Get the current level

        Returns:
            int: _description_
        """
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def draw_tree(root):
        dot = Graph()
        dot.node(str(root.val))
        add_edges(dot, root)
        return dot
