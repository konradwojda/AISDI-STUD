from bst import Node, BST
import pytest


def test_create_node():
    node = Node()
    assert node.left_child is None
    assert node.right_child is None
    assert node.parent is None
    assert node.value is None


def test_bst_create_from_values():
    values = [2, 1, 4, 6, 0]
    bst = BST(values=values)
    assert bst.root.value == 2
    assert bst.root.left_child.value == 1
    assert bst.root.left_child.left_child.value == 0
    assert bst.root.right_child.value == 4
    assert bst.root.right_child.right_child.value == 6


def test_bst_create_from_root():
    root = Node(value=10)
    bst = BST(root=root)
    assert bst.root.value == 10


def test_bst_failure():
    values = [12, 3, 4, 45]
    root = Node(value=10)
    with pytest.raises(ValueError):
        BST(root, values)


def test_bst_find():
    values = [2, 1, 4, 6, 0]
    bst = BST(values=values)
    assert bst.root.value == 2
    assert bst.root.left_child.value == 1
    assert bst.root.left_child.left_child.value == 0
    assert bst.root.right_child.value == 4
    assert bst.root.right_child.right_child.value == 6
    find = bst.find(4)
    assert find.right_child.value == 6
    assert find.parent.value == 2


def test_bst_find_min():
    values = [2, 1, 4, 6, 0]
    bst = BST(values=values)
    assert bst.root.value == 2
    assert bst.root.left_child.value == 1
    assert bst.root.left_child.left_child.value == 0
    assert bst.root.right_child.value == 4
    assert bst.root.right_child.right_child.value == 6
    min_val = bst.find_min_key()
    assert min_val.value == 0
    assert min_val.parent.value == 1
    assert min_val.left_child is None
    assert min_val.right_child is None


def test_bst_find_max():
    values = [2, 1, 4, 6, 0]
    bst = BST(values=values)
    assert bst.root.value == 2
    assert bst.root.left_child.value == 1
    assert bst.root.left_child.left_child.value == 0
    assert bst.root.right_child.value == 4
    assert bst.root.right_child.right_child.value == 6
    max_val = bst.find_max_key()
    assert max_val.value == 6
    assert max_val.parent.value == 4
    assert max_val.left_child is None
    assert max_val.right_child is None


def test_bst_find_succesor():
    values = [10, 5, 15, 2, 6, 17, 12]
    bst = BST(values=values)
    node = bst.root.right_child.left_child
    succesor = bst.find_succesor(node)
    assert succesor.value == 15
    assert succesor.parent.value == 10
    assert succesor.right_child.value == 17
    assert succesor.left_child.value == 12


def test_bst_find_predecessor():
    values = [10, 5, 15, 2, 6, 17, 12]
    bst = BST(values=values)
    node = bst.root.right_child.left_child
    predecessor = bst.find_predecessor(node)
    assert predecessor.value == 10
    assert predecessor.parent is None
    assert predecessor.right_child.value == 15
    assert predecessor.left_child.value == 5


def test_bst_add():
    values = [10, 5, 15, 2, 6, 17, 12]
    bst = BST(values=values)
    bst.add(25)
    assert bst.root.right_child.right_child.right_child.value == 25
    assert bst.root.right_child.right_child.right_child.parent.value == 17
    assert bst.root.right_child.right_child.right_child.right_child is None
    assert bst.root.right_child.right_child.right_child.left_child is None


def test_bst_remove_easy_case():
    values = [10, 5, 15, 2, 6, 17, 12]
    bst = BST(values=values)
    bst.remove_node(17)
    assert bst.root.right_child.right_child is None


def test_bst_remove_one_child():
    values = [10, 5, 15, 2, 6, 12]
    bst = BST(values=values)
    bst.remove_node(15)
    assert bst.root.right_child.value == 12
    assert bst.root.right_child.left_child is None
    assert bst.find(15) is None


def test_bst_remove_two_children():
    values = [10, 5, 15, 2, 6, 17, 12]
    bst = BST(values=values)
    bst.remove_node(15)
    assert bst.root.right_child.value == 17
    assert bst.root.right_child.left_child.value == 12
    assert bst.root.right_child.right_child is None
    assert bst.find(15) is None
