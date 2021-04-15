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
                    node.left_child = Node(parent=node, value=value)
                    break
                node = node.left_child
            else:
                if node.right_child is None:
                    node.right_child = Node(parent=node, value=value)
                    break
                node = node.right_child

    def find_min_key(self, node=None):
        node = node if node else self.root
        while node.left_child is not None:
            node = node.left_child
        return node

    def find_max_key(self, node=None):
        node = node if node else self.root
        while node.right_child is not None:
            node = node.right_child
        return node


if __name__ == "__main__":
    tree = BST()
    tree.add(56)
    tree.add(32)
    tree.add(86)
    tree.add(11)
    tree.add(45)
    tree.add(73)
    tree.add(98)
    print(tree.find_max_key().value)
    print(tree.find_min_key().value)
