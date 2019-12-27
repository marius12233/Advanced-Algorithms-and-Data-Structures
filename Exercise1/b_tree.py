from TdP_collections.tree.tree import Tree
from TdP_collections.map.red_black_tree import RedBlackTreeMap

class BTree(Tree):

    class Node():

        __slots__='_tree', '_parent', '_children'

        def __init__(self, tree=None):
            if tree is None:
                self._tree = RedBlackTreeMap()
            else:
                self._tree = tree
            self._parent = None
            self._children = self._tree._l

        def tree(self):
            return self._tree

        def children(self):
            return self._children

        def elements(self):
            for pos in self._tree.breadthfirst():
                yield pos.key()


    def __init__(self, a=2, b=4, degree=4):
        self._root = None
        self._size = 0
        self._num_node = 0
        self._a = degree//2
        self._b = degree

    def search(self, tree_node, k):
        tree = tree_node.tree()
        p = tree._subtree_search(tree.root(), k)
        if k == p.key():
            return p, tree_node
        if k < p.key():
            left_child =  p._node._left_out
            if left_child._node._child is None:
                return p, tree_node
            left_child = left_child._node._child
            #tree_node = left_child.tree()
            return self.search(left_child, k)
        else:
            right_child =  p._node._right_out
            print("Right child: ",right_child._node._child)
            if right_child._node._child is None:     #Non ha un figlio destro
                return (p, tree_node)
            right_child = right_child._node._child
            #tree_node = right_child.tree()
            return self.search( right_child, k)

    def delete(self, k):
        p, tree_node = self.search(self._root, k)
        if tree_node.tree().is_leaf(p):                             # p è già una foglia

            new_p, new_tree_node = self._predecessor_external_subtree(p, tree_node, k)
        else:
            if p._node._left_out._node._child is not None:
                new_p, new_tree_node = self.search(p._node._left_out._node._child, k)
            else:
                if p._node._left is not None:
                    new_p = tree_node.tree()._subtree_last_position(tree_node.tree().left(p))
                else:
                    new_p = tree_node.tree()._subtree_last_position(tree_node.tree().right(p))

                # new_p adesso è una foglia del suo rbtree
                new_p, new_tree_node = self._predecessor_external_subtree(new_p, tree_node, k)

        p._node._element = new_p._node._element
        new_tree_node.tree().delete(new_p)

        return new_p, new_tree_node


    def _predecessor_external_subtree(self, p, tree_node, k):
        if p._node._left_out._node._child  is None and p._node._right_out._node._child  is None:  # E' una foglia e non ha figli esterni
            return p, tree_node
        else:
            new_p, new_tree_node = None, None
            if p._node._left_out._node._child is not None:
                new_p, new_tree_node = self.search(p._node._left_out._node._child, k)
            elif p._node._right_out._node._child is not None:
                new_p, new_tree_node = self.search(p._node._right_out._node._child, k)
            return new_p, new_tree_node


    def add(self, k):
        if self._size==0:
            node = self.Node()
            self._root = node
            node.tree().add(k)
            self._size+=1
            self._num_node+=1
        else:
            (p, tree_node) = self.search(self._root, k)
            if p.key() == k:
                raise KeyError("Already exists a key k")
            tree_node.tree().add(k)
            self._size+=1
            self.check_overflow(tree_node)


    def check_overflow(self, tree_node):
        if len(tree_node.tree()) > self._b -1:
            print("Size: ", len(tree_node.tree()))
            print("Overflow!")
            self.split(tree_node)


    def split(self, tree_node):
        # Qui mi serve il mediano (p = median(tree_node))
        p = (tree_node.tree().root())

        T1, T2 = tree_node.tree().split(p)

        #parent = tree_node._parent

        #tree_node._parent = tree_node

        #Creo un nuovo albero
        node_left = self.Node(T1)
        node_right = self.Node(T2)

        print("Node left: ", node_left.tree().root().key())
        print("Node right: ", node_right.tree().root().key())
        print("Tree Node parent ", tree_node._parent)

        if tree_node._parent is None:   #Sono la radice
            print("Cambio figlio della radice")
            tree_parent = RedBlackTreeMap()
            tree_parent.add(p.key())
            node_parent = self.Node(tree_parent)
            self._root = node_parent
            tree_node._parent = tree_node
            node_parent._children.first()._node._child = node_left
            node_left._parent = node_parent
            node_parent._children.last()._node._child = node_right
            node_right._parent = node_parent
            self._num_node += 2

            #parent._child = node_parent
        else:
            node_parent = tree_node._parent
            new_p = node_parent.tree().add(p.key())
            new_p._node._left_out._node._child = node_left
            node_left._parent = node_parent
            new_p._node._right_out._node._child = node_right
            node_right._parent = node_parent
            self._num_node += 1
            self.check_overflow(node_parent)

    def root(self):
        return self._root

    def children(self, node):
        for nod in node.children():
            yield nod



if __name__=='__main__':

    btree = BTree()
    btree.add(10)
    print(btree.root().tree().root().key())
    for child in btree.children(btree.root()):
        print(child)
    btree.add(15)
    btree.add(5)
    btree.add(20)
    #print(btree.root().tree().right(btree.root().tree().root()))
    for child in btree.children(btree.root()):
        print(child)

    print("Nodi nella radice")

    for elems in btree.root().elements():
        print(elems)

    children_list = btree.root().children()
    node1 = children_list.first()._node._child
    node2 = children_list.last()._node._child
    print(type(node1))
    print("Nodo sx")
    for elems in node1.elements():
        print(elems)

    print("Nodo dx")
    for elems in node2.elements():
        print(elems)

    btree.add(25)
    btree.add(30)
    btree.add(50)
    btree.add(60)
    btree.add(70)
    btree.add(80)

    p, treeNode = btree.delete(80)


    print("DELETION")

    print(p.key())
    print(treeNode.tree()._size)
    print("# elements: ",btree._size)
    print("# nodes: ", btree._num_node)



    # children_list = btree.root().children()
    # node1 = children_list.first()._node._child
    # #node4 = children_list.before(children_list.before(children_list.last()))._node._child
    # #node3 = children_list.before(children_list.last())._node._child
    # node2 = children_list.last()._node._child
    #
    # print(len(children_list))
    #
    # print("After 25 e 30")
    #
    # print("Nodi nella radice")
    #
    # for elems in btree.root().elements():
    #     print(elems)
    #
    #
    # print("Nodo sx")
    # for elems in node1.elements():
    #     print(elems)

    #
    # print("Nodo mediano sx")
    # for elems in node4.elements():
    #     print(elems)
    #
    #
    # print("Nodo mediano dx")
    # for elems in node3.elements():
    #     print(elems)
    #

    # print("Nodo dx ")
    # for elems in node2.elements():
    #     print(elems)
    #
    # print("Second level: ")
    # children_left = node1.children()
    # print("Size childrens second level: ", len(children_left))
    # node_left = children_left.first()._node._child
    # node_right = children_left.after(children_left.first())._node._child
    # print("Nodo sx sx")
    # for elems in node_left.elements():
    #     print(elems)
    # print("Nodo sx dx")
    # for elems in node_right.elements():
    #     print(elems)
    #
    # children_right = node2.children()
    # node_right = children_right.last()._node._child
    # node_med = children_right.before(children_left.last())._node._child
    # node_left = children_right.before(children_right.before(children_left.last()))._node._child
    # print("Nodo dx sx")
    # for elems in node_left.elements():
    #     print(elems)
    # print("Nodo dx med")
    # for elems in node_med.elements():
    #     print(elems)
    # print("Nodo dx dx")
    # for elems in node_right.elements():
    #     print(elems)




