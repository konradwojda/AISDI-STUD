from bst import BST


class AVL(BST):
    def __init__(self):
        super().__init__()

    def add(self, value):
        node = super().add(value)
        self._check_balance(node)

    def _check_balance(self, node):
        current_node = node
        while current_node:
            if current_node.balance > 1 or current_node.balance < -1:
                self._repair_balance(current_node)

            if current_node.parent:
                if current_node.parent.left_child == current_node:
                    current_node.parent.balance += 1
                else:
                    current_node.parent.balance -= 1

                if current_node.parent.balance != 0:
                    current_node = current_node.parent
                    continue
            current_node = None

    def _repair_balance(self, node):
        if node.balance > 0:
            if node.left_child.balance < 0:
                self._left_rotation(node.left_child)
            self._right_rotation(node)
        elif node.balance < 0:
            if node.right_child.balance > 0:
                self._right_rotation(node.right_child)
            self._left_rotation(node)

    def _left_rotation(self, node):
        pivot = node.right_child

        node.right_child = node.left_child
        if pivot.left_child:
            pivot.left_child.parent = node

        pivot.left_child, node.parent = self._rotate(node, pivot)

        # node.rebalance()
        # pivot.rebalance()

        node.balance = node.balance - 1 - max(0, pivot.balance)
        pivot.balance = pivot.balance - 1 + min(0, node.balance)

    def _right_rotation(self, node):
        pivot = node.left_child

        node.left_child = node.left_child
        if pivot.left_child:
            pivot.left_child.parent = node

        pivot.right_child, node.parent = self._rotate(node, pivot)

        # node.rebalance()
        # pivot.rebalance()

        node.balance = node.balance + 1 - min(0, pivot.balance)
        pivot.balance = pivot.balance + 1 + max(0, node.balance)

    def _rotate(self, node, pivot):
        pivot.parent = node.parent
        if node.parent.left_child == node:
            node.parent.left_child = pivot
        elif node.parent:
            node.parent.right_child = pivot
        else:
            self.root = pivot
        return node, pivot


if __name__ == "__main__":
    tree = AVL()
    tree.add(56)
    tree.add(32)
    tree.add(86)
    tree.add(11)
    tree.add(45)
    tree.add(73)
    tree.add(98)
    print(tree.find_max_key().value)
    print(tree.find_min_key().value)
