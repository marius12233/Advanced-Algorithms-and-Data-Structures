from TdP_collections.tree.tree import Tree
from TdP_collections.map.red_black_tree import RedBlackTreeMap
from TdP_collections.queue.array_queue import ArrayQueue


class BTree(Tree):

    class Node():

        __slots__='_tree', '_parent', '_list_parent', '_children'

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

        def is_empty(self):
            return self._size==0

        def elements(self):
            for pos in self._tree.breadthfirst():
                yield pos.key()

        def positions(self):
            for pos in self._tree.breadthfirst():
                yield pos


    def __init__(self, degree=4):
        self._root = None
        self._size = 0
        self._num_node = 0
        self._a = (degree+1)//2
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
           # print("Right child: ",right_child._node._child)
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
            if p._node._left_out is not None and p._node._left_out._node._child is not None:
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
        self._size -=1

        self.check_underflow(tree_node)

        #return new_p, new_tree_node


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


    def check_overflow(self, tree_node, split_root=False):
        if len(tree_node.tree()) > self._b -1:
            print("Size: ", len(tree_node.tree()))
            print("Overflow!")
            self.split(tree_node)

    def check_underflow(self, tree_node):
        print("SIZE AFTER DELETE: ", len(tree_node.tree()._l))
        print("MINIMO: ", self._a)

        if len(tree_node.tree()._l) < self._a:
            print("UNDERFLOW!!!")

            self.resolve_underflow(tree_node)

    def _immediate_siblings(self, tree_node):
        if self._root == tree_node:
            return None
        child_pos = tree_node._list_parent
        print("Child position: ", child_pos)
        children = tree_node._parent.children()

        tnode_before, tnode_after = None, None

        if not child_pos == children.first():
            tnode_before = children.before(child_pos)._node._child

        if not child_pos == children.last():
            tnode_after = children.after(child_pos)._node._child

        return tnode_before, tnode_after



    def resolve_underflow(self, tree_node):
        tbefore, tafter = self._immediate_siblings(tree_node)
        if tbefore is not None and len(tbefore.tree()._l) > self._a:
            self.transfer(tree_node, tbefore)
        elif tafter is not None and len(tafter.tree()._l) > self._a:
            self.transfer(tree_node, tafter, before=False)
        else:
            if tbefore is not None:
                print("FUSION LEFT")
                self.fusion(tree_node, tbefore, left=True)
            elif tafter is not None:
                print("FUSION RIGHT")
                self.fusion(tree_node, tafter, left=False)

    def transfer(self, tree_node, tree_transfer_node, before=True):
        w = tree_node
        s = tree_transfer_node
        u = tree_node._parent
        p_parent = tree_node._list_parent._node._parent
        #tree_node.add(p_parent.key())
        if before:
            p_transfer = tree_transfer_node.tree()._subtree_last_position(tree_transfer_node.tree().root())
        else:
            p_transfer = tree_transfer_node.tree()._subtree_first_position(tree_transfer_node.tree().root())
        w.tree().add(p_parent.key())
        p_parent._node._element = p_transfer._node._element
        s.tree().delete(p_transfer)

    def fusion(self, tree_node, tree_fusion_node, left=True):
        # if left == True s is at left of w
        w = tree_node
        s = tree_fusion_node
        u = w._parent
        p_parent = w._list_parent._node._parent
        tree = RedBlackTreeMap()
        p = tree.add(p_parent.key())
        if left:

            w._tree.catenate(w._tree, p, left=False, T2=s._tree)
            #w._children = s._tree._l
            #w.add(p_parent.key())

        else:
            s.add(p_parent.key())

        u.tree().delete(p_parent)




    def split(self, tree_node):
        # Qui mi serve il mediano (p = median(tree_node))
        #p = (tree_node.tree().root())
        p = tree_node.tree()._get_median()

        if tree_node._parent is None:
            T1, T2 = tree_node.tree().split(p, split_root=True)
        else:
            T1, T2 = tree_node.tree().split(p, split_root=False)

        #parent = tree_node._parent

        #tree_node._parent = tree_node

        #Creo un nuovo albero
        node_left = self.Node(T1)
        node_right = self.Node(T2)


        if tree_node._parent is None:   #Sono la radice
            print("===================================== SPLIT RADIX ===============================================")
            tree_parent = RedBlackTreeMap()
            np = tree_parent.add(p.key())
            node_parent = self.Node(tree_parent)
            self._root = node_parent
            tree_node._parent = tree_node

            np._node._left_out._node._child = node_left
            node_left._parent = node_parent
            node_left._list_parent = np._node._left_out

            self._update_children(node_left)

            np._node._right_out._node._child = node_right
            node_right._parent = node_parent
            node_right._list_parent = np._node._right_out

            self._update_children(node_right)

            self._num_node += 2

            #parent._child = node_parent
        else:
            print("========================== SPLIT NO RADIX ===============================")
            node_parent = tree_node._parent
            new_p = node_parent.tree().add(p.key())

            new_p._node._left_out._node._child = node_left
            node_left._parent = node_parent
            node_left._list_parent = new_p._node._left_out

            self._update_children(node_left)


            new_p._node._right_out._node._child = node_right
            node_right._parent = node_parent
            node_right._list_parent = new_p._node._right_out

            self._update_children(node_right)


            self._num_node += 1
            self.check_overflow(node_parent)



    def _update_children(self, node):
        children = node.children()
        if children.first() is not None and children.first()._node is not None and children.first()._node._child is not None:
            for child in node.children():
                child._node._child._parent = node


    def root(self):
        return self._root

    def children(self, node):
        for nod in node.children():
            yield nod

    def bfs(self, tree_node):
        for elem in tree_node.elements():
            yield elem







if __name__=='__main__':



    btree = BTree(degree=7)
    btree.add(10)
    btree.add(15)
    btree.add(5)
    btree.add(20)
    #
    btree.add(30)
    btree.add(40)
    # print("============ add 25....")
    btree.add(25)
    btree.add(60)
    btree.add(55)

    print("========== add 70")
    btree.add(70)
    # # # #btree.add(18)
    print("========== add 55")
    # # # btree.add(19)
    print("========== add 80")
    btree.add(80)
    btree.add(85)
    btree.add(90)
    btree.add(95)
    btree.add(100)
    btree.delete(100)
    #btree.delete(95)
    print(" ADDING 100 ...")
    children_list = btree.root().children()

    print("=========== LISTA RADICE ================")

    print("LEN L: ", len(children_list))


    for pos in children_list:
        print("Parent: ", pos._node._parent.key())
        print("Leaf: ", btree.root()._tree.is_leaf(pos._node._parent))
        print(pos)

    node1 = children_list.first()._node._child #children_list.before(children_list.last())._node._child
    node2 = children_list.last()._node._child
    print("============= LISTA N1 ===============0")
    print("LEN L: ", len(node1._tree._l))
    print("Elements")
    for pos in node1._tree._l:
        print(pos)
        print(pos._node._parent.key())
        print("Leaf: ",node1._tree.is_leaf(pos._node._parent))
        print("IS LEFT OUT?: ", pos._node._parent._node._left_out == pos)
        print("IS right OUT?: ", pos._node._parent._node._right_out == pos)
        if pos._node._parent._node._left is not None:
            print("Left: ", node1._tree.left(pos._node._parent).key())
        if pos._node._parent._node._right is not None:
            print("Right: ", node1._tree.right(pos._node._parent).key())
        print("IS MEDIAN: ", node1._tree._l._median == pos._node,  node1._tree._l._median._parent.key())


    print("============= LISTA N2 ===============0")
    print("LEN L: ", len(node2._tree._l))
    print("Elements")
    for pos in node2._tree._l:
        print(pos)
        print(pos._node._parent.key())
        print("Leaf: ",node2._tree.is_leaf(pos._node._parent))
        print("IS LEFT OUT?: ", pos._node._parent._node._left_out == pos)
        print("IS right OUT?: ", pos._node._parent._node._right_out == pos)
        if pos._node._parent._node._left is not None:
            print("Left: ", node2._tree.left(pos._node._parent).key())
        if pos._node._parent._node._right is not None:
            print("Right: ", node2._tree.right(pos._node._parent).key())
        print("IS MEDIAN: ", node2._tree._l._median == pos._node, node2._tree._l._median._parent.key())

    #btree.add(100)
    # btree.add(105)
    # btree.add(107)
    # btree.add(108)
    # btree.add(109)
    # btree.add(110)


    #btree.delete(80)
    #btree.delete(70)
    #btree.delete(60)
    #btree.delete(80)
    root = btree._root
    #
    # print("="*20, "ROOT", "="*20)
    #
    print("Elementi nella ROOT")
    for elems in root.positions():
        print(elems.key())
        print("BH: ",elems._node._black_height)

    print("Size: ", root._tree._size)
    #
    # children_list = btree.root().children()
    node1 = children_list.first()._node._child
    node2 = children_list.after(children_list.first())._node._child
    node22 = children_list.after(children_list.after(children_list.first()))._node._child
    node3 = children_list.before(children_list.last())._node._child
    node4 = children_list.last()._node._child
    #
    #
    print("Elementi Node left")
    for elems in node1.positions():
        print(elems.key(), "IS RED: ", elems._node._red)
        print("BH: ", elems._node._black_height)
    print("Size: ", node1._tree._size)
    #
    #
    print("Elementi Node right")
    for elems in node2.positions():
        print(elems.key(), "IS RED: ", elems._node._red)
        print("BH: ", elems._node._black_height)
    print("Size: ", node2._tree._size)



    #
    #
    #
    print("Elementi Node right")
    for elems in node22.positions():
        print(elems.key(), "IS RED: ", elems._node._red)
        print("BH: ", elems._node._black_height)
    print("Size: ", node22._tree._size)


    print("Elementi Node right")
    for elems in node3.positions():
        print(elems.key(), "IS RED: ", elems._node._red)
        print("BH: ", elems._node._black_height)

    print("Size: ", node3._tree._size)


    print("Elementi Node right")
    for elems in node4.positions():
        print(elems.key(), "IS RED: ", elems._node._red)
        print("BH: ", elems._node._black_height)

    print("Size: ", node4._tree._size)
    #node4 = children_list.before(children_list.before(children_list.last()))._node._child

    # children_list = btree.root().children()
    #
    # node1 = children_list.first()._node._child
    # node2 = children_list.last()._node._child
    #
    #
    # print("=" * 20, "LV1", "=" * 20)
    #
    # print("Node 1")
    # for elems in node1.elements():
    #     print(elems)
    #
    # print("Node 2")
    # for elems in node2.elements():
    #     print(elems)
    # print("Parent:")
    # parent = node1._parent
    # for elems in parent.elements():
    #     print(elems)
    #
    # print("LV2 dx")
    # children_list = node2.children()
    # node1 = children_list.before(children_list.before(children_list.last()))._node._child
    # node3 = children_list.last()._node._child
    # node2 = children_list.before(children_list.last())._node._child
    #
    # print("Node 1")
    # for elems in node1.elements():
    #     print(elems)
    # print("Node 2")
    # for elems in node2.elements():
    #     print(elems)
    # print("Node 3")
    # for elems in node3.elements():
    #     print(elems)
    # print("Parent:")
    # parent = node2._parent
    # for elems in parent.elements():
    #     print(elems)
    #
    #
    #


    # print("After fusion")
    #
    # print("Node 1")
    # for elems in node3.elements():
    #     print(elems)
    #
    # print("Node 2")
    # for elems in node2.elements():
    #     print(elems)

    #btree.add(60)




    # btree.add(10)
    # print(btree.root().tree().root().key())
    # for child in btree.children(btree.root()):
    #     print(child)
    # btree.add(15)
    # btree.add(5)
    # btree.add(20)
    # #print(btree.root().tree().right(btree.root().tree().root()))
    # for child in btree.children(btree.root()):
    #     print(child)
    #
    # print("Nodi nella radice")
    #
    # for elems in btree.root().elements():
    #     print(elems)
    #
    # children_list = btree.root().children()
    # node1 = children_list.first()._node._child
    # node2 = children_list.last()._node._child
    # print(type(node1))
    # print("Nodo sx")
    # for elems in node1.elements():
    #     print(elems)
    #
    # print("Nodo dx")
    # for elems in node2.elements():
    #     print(elems)
    #
    # btree.add(25)
    # btree.add(30)
    # btree.add(50)
    # btree.add(60)
    # btree.add(70)
    # btree.add(80)
    #
    # p, treeNode = btree.delete(80)
    #
    #
    # print("DELETION")
    #
    # print(p.key())
    # print(treeNode.tree()._size)
    # print("# elements: ",btree._size)
    # print("# nodes: ", btree._num_node)
    #
    # first, second = btree._immediate_siblings(treeNode)
    # parent = treeNode._parent
    # print("After deletion: ")
    # print(first.tree().root().key())
    # print(treeNode.tree().root().key())
    # print(parent.tree().root().key())
    #
    #
    # root = btree._root
    #
    # print("Parent elements")
    #
    #
    #
    # for elems in parent.elements():
    #     print(elems)
    #
    # print("Root elements")
    #
    #
    #
    #
    # for elems in root.elements():
    #     print(elems)





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




