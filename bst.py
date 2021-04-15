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

    def find_succesor(self, node=None):
        node = node if node else self.root
        if node.right_child is not None:
            return self.find_min_key(node.right_child)
        node_tmp = node.parent
        while node_tmp is not None and node_tmp.left_child != node:
            node = node_tmp
            node_tmp = node_tmp.parent
        return node_tmp

    def find_predecessor(self, node=None):
        node = node if node else self.root
        if node.left_child is not None:
            return self.find_max_key(node.left_child)
        node_tmp = node.parent
        while node_tmp is not None and node_tmp.right_child != node:
            node = node_tmp
            node_tmp = node_tmp.parent
        return node_tmp

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

    def remove_node(self, value):
        node = self.find(value)
        if node.left_child is None or node.right_child is None:
            y = node
        else:
            y = self.find_succesor(node)
        if y.left_child is not None:
            x = y.left_child
        else:
            x = y.right_child
        if x is not None:
            x.parent = y.parent
        if y.parent is None:
            self.root = x
        else:
            if y == y.parent.left_child:
                y.parent.left_child = x
            else:
                y.parent.right_child = x
        if y != node:
            node.value = y.value
        return y


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
    print(tree.find_succesor(tree.find(45)).value)
    tree.remove_node(56)
    print(tree.root.value)
