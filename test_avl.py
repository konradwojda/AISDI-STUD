from bst import Node
from avl import AVL
import pytest


def test_create_node():
    node = Node()
    assert node.left_child is None
    assert node.right_child is None
    assert node.parent is None
    assert node.value is None


def test_avl_create_from_values():
    values = [2, 1, 4, 6, 0]
    avl = AVL(values=values)
    assert avl.root.value == 2
    assert avl.root.left_child.value == 1
    assert avl.root.left_child.left_child.value == 0
    assert avl.root.right_child.value == 4
    assert avl.root.right_child.right_child.value == 6


def test_avl_create_from_root():
    root = Node(value=10)
    avl = AVL(root=root)
    assert avl.root.value == 10


def test_avl_failure():
    values = [12, 3, 4, 45]
    root = Node(value=10)
    with pytest.raises(ValueError):
        AVL(root, values)


def test_avl_find():
    values = [2, 1, 4, 6, 0]
    avl = AVL(values=values)
    assert avl.root.value == 2
    assert avl.root.left_child.value == 1
    assert avl.root.left_child.left_child.value == 0
    assert avl.root.right_child.value == 4
    assert avl.root.right_child.right_child.value == 6
    find = avl.find(4)
    assert find.right_child.value == 6
    assert find.parent.value == 2


def test_avl_find_min():
    values = [2, 1, 4, 6, 0]
    avl = AVL(values=values)
    assert avl.root.value == 2
    assert avl.root.left_child.value == 1
    assert avl.root.left_child.left_child.value == 0
    assert avl.root.right_child.value == 4
    assert avl.root.right_child.right_child.value == 6
    min_val = avl.find_min_key()
    assert min_val.value == 0
    assert min_val.parent.value == 1
    assert min_val.left_child is None
    assert min_val.right_child is None


def test_avl_find_max():
    values = [2, 1, 4, 6, 0]
    avl = AVL(values=values)
    assert avl.root.value == 2
    assert avl.root.left_child.value == 1
    assert avl.root.left_child.left_child.value == 0
    assert avl.root.right_child.value == 4
    assert avl.root.right_child.right_child.value == 6
    max_val = avl.find_max_key()
    assert max_val.value == 6
    assert max_val.parent.value == 4
    assert max_val.left_child is None
    assert max_val.right_child is None


def test_avl_find_succesor():
    values = [10, 5, 15, 2, 6, 17, 12]
    avl = AVL(values=values)
    node = avl.root.right_child.left_child
    succesor = avl.find_succesor(node)
    assert succesor.value == 15
    assert succesor.parent.value == 10
    assert succesor.right_child.value == 17
    assert succesor.left_child.value == 12


def test_avl_find_predecessor():
    values = [10, 5, 15, 2, 6, 17, 12]
    avl = AVL(values=values)
    node = avl.root.right_child.left_child
    predecessor = avl.find_predecessor(node)
    assert predecessor.value == 10
    assert predecessor.parent is None
    assert predecessor.right_child.value == 15
    assert predecessor.left_child.value == 5


def test_avl_add():
    values = [10, 5, 15, 2, 6, 17, 12]
    avl = AVL(values=values)
    avl.add(25)
    assert avl.root.right_child.right_child.right_child.value == 25
    assert avl.root.right_child.right_child.right_child.parent.value == 17
    assert avl.root.right_child.right_child.right_child.right_child is None
    assert avl.root.right_child.right_child.right_child.left_child is None


def test_avl_remove_easy_case():
    values = [10, 5, 15, 2, 6, 17, 12]
    avl = AVL(values=values)
    avl.remove_node(17)
    assert avl.root.right_child.right_child is None


def test_avl_remove_one_child():
    values = [10, 5, 15, 2, 6, 12]
    avl = AVL(values=values)
    avl.remove_node(15)
    assert avl.root.right_child.value == 12
    assert avl.root.right_child.left_child is None
    assert avl.find(15) is None


def test_avl_remove_two_children():
    values = [10, 5, 15, 2, 6, 17, 12]
    avl = AVL(values=values)
    avl.remove_node(15)
    assert avl.root.right_child.value == 17
    assert avl.root.right_child.left_child.value == 12
    assert avl.root.right_child.right_child is None
    assert avl.find(15) is None
