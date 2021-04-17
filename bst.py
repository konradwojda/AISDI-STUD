class Node:
    def __init__(self, left_child=None, right_child=None,
                 parent=None, value=None, balance=0):
        self.left_child = left_child
        self.right_child = right_child
        self.value = value
        self.parent = parent
        self.balance = balance

    def get_height(self):
        highest = max(self._left_height(), self._right_height())
        return highest + 1

    def _left_height(self):
        height = 0
        current_child = self.left_child
        while current_child:
            height += 1
            current_child = current_child.left_child
        return height

    def _right_height(self):
        height = 0
        current_child = self.right_child
        while current_child:
            height += 1
            current_child = current_child.right_child
        return height

    def rebalance(self):
        if self.right_child:
            right_height = self.right_child.get_height()
        else:
            right_height = 0
        if self.left_child:
            left_height = self.left_child.get_height()
        else:
            left_height = 0
        self.balance = right_height - left_height

    def to_string(self, depth=0):
        _str = ""
        if self.right_child:
            _str += self.right_child.to_string(depth + 1)
        _str += ' ' * 4 * depth + ">" + str(self.value) + "\n"
        if self.left_child:
            _str += self.left_child.to_string(depth + 1)
        return _str


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
            return self.root

        node = self.root
        while node is not None:
            if value < node.value:
                if node.left_child is None:
                    node.left_child = Node(parent=node, value=value)
                    continue
                node = node.left_child
            elif value > node.value:
                if node.right_child is None:
                    node.right_child = Node(parent=node, value=value)
                    continue
                node = node.right_child
            elif value == node.value:
                break
        return node

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

    def __str__(self):
        if not self.root:
            return ""
        return self.root.to_string()


if __name__ == "__main__":
    values = [10, 5, 15, 2, 6, 17, 12]
    bst = BST(values=values)
    print(bst)
