class Node:
    def __init__(self, left_child=None, right_child=None,
                 parent=None, value=None):
        self.left_child = left_child
        self.right_child = right_child
        self.value = value
        self.parent = parent


class BST:
    def __init__(self, root=None, values=None):
        if root and values:
            raise ValueError("Cannot create tree from both root and values")
        self.root = root
        if values is not None:
            for value in values:
                self.add(value)

    def find(self, value):
        node = self.root
        while node is not None and node.value != value:
            if value < node.value:
                node = node.left_child
            elif value > node.value:
                node = node.right_child
        return node

    def add(self, value):
        if self.root is None:
            self.root = Node(value=value)
            return
        node = self.root
        while node is not None:
            if value < node.value:
                if node.left_child is None:
                    break
                node = node.left_child
            elif value > node.value:
                if node.right_child is None:
                    break
                node = node.right_child
            else:
                return
        if value < node.value:
            node.left_child = Node(parent=node, value=value)
        else:
            node.right_child = Node(parent=node, value=value)
        return


if __name__ == "__main__":
    tree = BST()
    tree.add(56)
    tree.add(32)
    tree.add(86)
    tree.add(11)
    tree.add(45)
    tree.add(73)
    tree.add(98)
