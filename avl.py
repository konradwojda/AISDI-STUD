from bst import BST


class AVL(BST):
    def __init__(self, root=None, values=None):
        super().__init__(root, values)

    def add(self, value):
        node = super().add(value)
        self._check_balance(node)

    def _check_balance(self, node):
        while node:
            if node.balance < -1 or node.balance > 1:
                self._repair_balance(node)
                return

            if node.parent:
                if node.parent.left_child == node:
                    node.parent.balance -= 1
                else:
                    node.parent.balance += 1
                if node.parent.balance != 0:
                    node = node.parent
                    continue
            return

    def _repair_balance(self, node):
        if node.balance > 0:
            if node.right_child.balance < 0:
                self._right_rotation(node.right_child)
            self._left_rotation(node)

        elif node.balance < 0:
            if node.left_child.balance > 0:
                self._left_rotation(node.left_child)
            self._right_rotation(node)

    def _left_rotation(self, node):
        pivot = node.right_child
        node.right_child = pivot.left_child

        if pivot.left_child:
            pivot.left_child.parent = node

        pivot.parent = node.parent
        if node.parent is None:
            self.root = pivot
        elif node == node.parent.left_child:
            node.parent.left_child = pivot
        else:
            node.parent.right_child = pivot
        pivot.left_child = node
        node.parent = pivot

        node.rebalance()
        pivot.rebalance()

    def _right_rotation(self, node):
        pivot = node.left_child
        node.left_child = pivot.right_child

        if pivot.right_child:
            pivot.right_child.parent = node

        pivot.parent = node.parent
        if node.parent is None:
            self.root = pivot
        elif node == node.parent.right_child:
            node.parent.right_child = pivot
        else:
            node.parent.left_child = pivot

        pivot.right_child = node
        node.parent = pivot

        node.rebalance()
        pivot.rebalance()


if __name__ == "__main__":
    values = [
        1, 2, 56, 2, 67, 22, 567, 223, 435,
        7, 34, 24, 12, 6724, 2341, 23, 15, 34]
    tree = AVL(values=values)
    tree.add(5)
    print(tree)
