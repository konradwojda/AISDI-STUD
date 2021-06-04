from typing import List


class Node:
    def __init__(self, position, cost):
        self._position = position
        self._cost = cost
        self._adjacents = []
        self._visited = False
        self._previous = None
        self._visible = False

    def add_adjacent(self, adjacent_node):
        self._adjacents.append(adjacent_node)

    def get_position(self):
        return self._position

    def get_cost(self):
        return self._cost

    def get_adjacents(self):
        return self._adjacents

    def set_visited(self):
        self._visited = True

    def is_visited(self):
        return self._visited

    def set_visible(self):
        self._visible = True

    def is_visible(self):
        return self._visible

    def set_previous(self, other_node):
        self._previous = other_node

    def get_previous(self):
        return self._previous


def make_table(file_handle):
    str_table = file_handle.read()
    return [list(i) for i in str_table.split('\n')]


def create_nodes(table):
    nodes = []
    for i in range(len(table)):
        sub_nodes = []
        for j in range(len(table[i])):
            new_node = Node((i, j), int(table[i][j]))
            sub_nodes.append(new_node)
        nodes.append(sub_nodes)
    return nodes


def add_adjacents(nodes):
    for i in range(len(nodes)):
        for j in range(len(nodes[i])):
            node = nodes[i][j]
            if j != 0:
                node.add_adjacent(nodes[i][j-1])
            if j != len(nodes[i])-1:
                node.add_adjacent(nodes[i][j+1])
            if i != 0:
                node.add_adjacent(nodes[i-1][j])
            if i != len(nodes)-1:
                node.add_adjacent(nodes[i+1][j])


# in_tuples = 0 -> output list of nodes [Node, Node, Node, ...]
# in_tuples = 1 -> output list of nodes [(Node, cost), (Node, cost), ...]
def get_nodes(file_, in_tuples=0):
    with open(file_, 'r') as fh:
        table = make_table(fh)
    nodes = create_nodes(table)
    add_adjacents(nodes)
    out_nodes = []
    for sub_nodes in nodes:
        for node in sub_nodes:
            if in_tuples:
                out_nodes.append((node, node.get_cost))
            else:
                out_nodes.append(node)
    return out_nodes


def dijkstra(nodes: List):
    start = None
    end = None
    visited_nodes = set()
    not_visited = set()
    costs_dict = {}
    prevorius_nodes_dict = {}
    for node in nodes:
        costs_dict[node] = float("inf")
        prevorius_nodes_dict[node] = -1
        if node.get_cost() == 0:
            if start is None:
                start = node
            else:
                end = node
    costs_dict[start] = 0
    not_visited = set(nodes)
    while len(not_visited) != 0:
        queue = sorted(not_visited, key=lambda node: costs_dict[node])
        visited_nodes.add(queue[0])
        not_visited.remove(queue[0])
        for neighbour in queue[0].get_adjacents():
            if neighbour in not_visited:
                neighbour.set_visited()
                if costs_dict[neighbour] > costs_dict[queue[0]] + neighbour.get_cost():
                    costs_dict[neighbour] = costs_dict[queue[0]] + neighbour.get_cost()
                    prevorius_nodes_dict[neighbour] = queue[0]
    temp = end
    while temp != start:
        temp.set_visible()
        prev = prevorius_nodes_dict[temp]
        temp = prev
    start.set_visible()
    start.set_visited()
    return nodes


def print_nodes(nodes: list, width):
    text = ''
    for i, node in enumerate(nodes):
        if node.is_visible() and node.is_visited():
            text += str(node.get_cost())
        elif node.is_visited():
            text += '*'
        else:
            text += ' '
        if i % width == width - 1:
            text += '\n'
    return text[:len(text) - 1]


if __name__ == "__main__":
    nodes = get_nodes("test.txt")
    nodes = dijkstra(nodes)
    print(print_nodes(nodes, 6))
    print("dupa")