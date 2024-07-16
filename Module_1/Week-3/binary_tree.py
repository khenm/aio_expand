from graphviz import Graph
from collections import deque


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def add_edges(dot, node):
    if node is None:
        return
    if node.left:
        dot.edge(str(node.val), str(node.left.val))
        add_edges(dot, node.left)
    if node.right:
        dot.edge(str(node.val), str(node.right.val))
        add_edges(dot, node.right)


def draw_tree(root):
    dot = Graph()
    dot.node(str(root.val))
    add_edges(dot, root)
    return dot


def breadth_first_search(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # BFS
    bfs_result = breadth_first_search(root)
    print("BFS Traversal Result: ", bfs_result)
