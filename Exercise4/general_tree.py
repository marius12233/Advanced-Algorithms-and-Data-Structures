from TdP_collections.graphs.graph import Graph
from Exercise4.install_software import *

class GeneralTree(Graph):

    def __init__(self):
        super(GeneralTree, self).__init__()
        self._root = None
        self._parent = {}

    def root(self):
        return self._root
        
    def parent(self, v):
        return self._parent[v]

    def is_root(self, v):
        return self._root == v
        
    def is_leaf(self, v):
        count = 0
        for e in self.children(v):
            count+=1
        if count == 0:
            return True
        return False
    
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