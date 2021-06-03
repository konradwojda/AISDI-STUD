class Node:
    def __init__(self, position, cost):
        self._position = position
        self._cost = cost
        self._adjacents = []
        self._visited = False
        self._previous = None

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
