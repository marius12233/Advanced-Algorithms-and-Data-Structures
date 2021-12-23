from TdP_collections.graphs.graph import Graph
from install_software import *

class GeneralTree(Graph):

    def __init__(self):
        super(GeneralTree, self).__init__()
        self._root = None
        self._parent = {}

    def root(self):
        return self._root

    def is_root(self, v):
        return self._root == v

    def add_root(self, x):
        root = self.insert_vertex(x)
        self._root=root
        self._parent[root]=None
        return root

    def add_child(self, v, x):
        child = self.insert_vertex(x)
        self.insert_edge(v, child)
        self._parent[child] = v
        return child

    def children(self, v):
        for e in self.incident_edges(v):
            adj = e.opposite(v)
            if not adj == self._parent[v]:
                yield adj

    def parent(self, v):
        return self._parent[v]

    def is_leaf(self, v):
        count = 0
        for e in self.children(v):
            count+=1
        if count == 0:
            return True
        return False


if __name__ == "__main__":
    tree = GeneralTree()
    root = tree.add_root(1)
    a = tree.add_child(root, 2)
    b = tree.add_child(root, 3)
    c = tree.add_child(root, 4)
    d = tree.add_child(a, 5)
    e = tree.add_child(a, 6)
    f = tree.add_child(b, 7)
    g = tree.add_child(b, 8)

    sol = min_nodes_install(tree)

    #forest = DFS_complete(tree)

    #
    # for k in sol.keys():
    #     print(type(k), "\t", k.element())
    #     #print(k, " ", type(forest[k]))










    # for v in dp.keys():
    #     print(v, "   ", dp[v])











