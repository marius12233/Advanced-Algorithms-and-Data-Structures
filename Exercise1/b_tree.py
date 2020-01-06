from TdP_collections.tree.tree import Tree
from TdP_collections.map.red_black_tree import RedBlackTreeMap
from TdP_collections.queue.array_queue import ArrayQueue


class BTree(Tree):
    """This class implements the external structure"""

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


    def __init__(self, degree=7):
        """Setting of B-Tree parameters."""
        self._root = None
        self._size = 0
        self._num_node = 0
        self._a = (degree+1)//2
        self._b = degree


    def search(self, tree_node, k):
        """It searches for the k-key node through all the elements of the B-Tree"""
        tree = tree_node.tree()
        p = tree._subtree_search(tree.root(), k)

        if k == p.key():
            #key finding
            return p, tree_node
        if k < p.key():
            #key research through the left subtree
            left_child =  p._node._left_out
            if left_child._node._child is None:
                return p, tree_node
            left_child = left_child._node._child
            #tree_node = left_child.tree()
            return self.search(left_child, k)
        else:
            #key research through the right subtree
            right_child =  p._node._right_out
           # print("Right child: ",right_child._node._child)
            if right_child._node._child is None:     #Non ha un figlio destro
                return (p, tree_node)
            right_child = right_child._node._child
            #tree_node = right_child.tree()
            return self.search( right_child, k)

    def delete(self, k):
        """It proceeds with the deletion of the k-node in the B-Tree structure"""
        print("DELETING ", k)
        p, tree_node = self.search(self._root, k)
        if tree_node.tree().is_leaf(p): #leaf node
            #research of the k-node in the outer subtree
            new_p, new_tree_node = self._predecessor_external_subtree(p, tree_node, k)
        else:
            if p._node._left_out is not None and p._node._left_out._node._child is not None:
                #the research continues in the left child of the B-Tree node
                new_p, new_tree_node = self.search(p._node._left_out._node._child, k)
            else:
                if p._node._left is not None:
                    #research through its internal left child
                    new_p = tree_node.tree()._subtree_last_position(tree_node.tree().left(p))
                else:
                    #research through its internal right child
                    new_p = tree_node.tree()._subtree_last_position(tree_node.tree().right(p))

                # new_p adesso è una foglia del suo rbtree
                new_p, new_tree_node = self._predecessor_external_subtree(new_p, tree_node, k)

        p._node._element = new_p._node._element
        new_tree_node.tree().delete(new_p)
        self._size -=1

        #if not k==40:
        self.check_underflow(new_tree_node)

        #return new_p, new_tree_node


    def _predecessor_external_subtree(self, p, tree_node, k):
        """
        Find a position with key k in the external subtree
        :param p: position from start the search
        :param tree_node: the tree_node
        :param k:
        :return:
        """
        if p._node._left_out._node._child  is None and p._node._right_out._node._child  is None:  # E' una foglia e non ha figli esterni
            return p, tree_node
        else:
            new_p, new_tree_node = None, None
            if p._node._left_out._node._child is not None:
                new_p, new_tree_node = self.search(p._node._left_out._node._child, k)
            elif p._node._right_out._node._child is not None:
                new_p, new_tree_node = self.search(p._node._right_out._node._child, k)
            return new_p, new_tree_node


    def add(self, k, v=None):
        print("\nADDING: ",k,"\n")
        if self._size==0:
            node = self.Node()
            self._root = node
            node.tree().add(k, v)
            self._size+=1
            self._num_node+=1
        else:
            (p, tree_node) = self.search(self._root, k)
            if p.key() == k:
                raise KeyError("Already exists a key k")
            tree_node.tree().add(k, v)
            self._size+=1
            self.check_overflow(tree_node)


    def check_overflow(self, tree_node, split_root=False):
        if len(tree_node.tree()) > self._b -1:
            self.split(tree_node)

    def check_underflow(self, tree_node):
        """It checks underflow conditions, comparing the length of the tree to a parameter"""
        if len(tree_node.tree()._l) < self._a:
            print("UNDERFLOW at node with root: ",tree_node.tree().root())
            self.resolve_underflow(tree_node)

    def _immediate_siblings(self, tree_node):
        """It returns the adjacent subtrees of tree_node"""
        if self._root == tree_node:
            return None
        child_pos = tree_node._list_parent
        children = tree_node._parent.children()

        tnode_before, tnode_after = None, None

        if not child_pos == children.first():
            #setting of the left adjacent subtrees
            tnode_before = children.before(child_pos)._node._child

        if not child_pos == children.last():
            #setting of the right adjacent subtrees
            tnode_after = children.after(child_pos)._node._child

        return tnode_before, tnode_after



    def resolve_underflow(self, tree_node):
        """The method is called to solve an underflow condition"""
        tbefore, tafter = self._immediate_siblings(tree_node)
        if tbefore is not None and len(tbefore.tree()._l) > self._a:
            #transfer calling on the left adjacent subtrees
            print("TRANSFER FROM LEFT")
            self.transfer(tree_node, tbefore)
        elif tafter is not None and len(tafter.tree()._l) > self._a:
            #transfer calling on the right adjacent subtrees
            print("TRANSFER FROM RIGHT")
            self.transfer(tree_node, tafter, before=False)
        else:
            p_parent = tree_node._list_parent._node._parent
            if tbefore is not None and p_parent._node._right_out is not None and tree_node._list_parent._node == p_parent._node._right_out._node: #
                print("FUSION LEFT")
                #fusion calling on the left adjacent subtrees
                self.fusion(tree_node, tbefore, left=True)
            elif tafter is not None:
                print("FUSION RIGHT")
                #fusion calling on the right adjacent subtrees
                self.fusion(tree_node, tafter, left=False)

    def transfer(self, tree_node, tree_transfer_node, before=True):
        """It solves an underflow condition by exploiting the adjacent subtrees"""
        w = tree_node
        s = tree_transfer_node
        u = tree_node._parent
        w_parent = tree_node._list_parent._node._parent #Position del nodo nell'albero di cui è figlio tree node
        s_parent = s._list_parent._node._parent
        #tree_node.add(p_parent.key())
        if before:
            #last node calling, in case of left subtree
            p_transfer = tree_transfer_node.tree()._subtree_last_position(tree_transfer_node.tree().root())
        else:
             #first node calling, in case of rigth subtree
            p_transfer = tree_transfer_node.tree()._subtree_first_position(tree_transfer_node.tree().root())
        # if w_parent
        if w_parent == s_parent:
            w.tree().add(w_parent.key())
            w_parent._node._element = p_transfer._node._element
        else:
            parent = u.tree().before(w_parent) if before else u.tree().after(w_parent)
            w.tree().add(parent.key())
            parent._node._element = p_transfer._node._element

        s.tree().delete(p_transfer)

    def fusion(self, tree_node, tree_fusion_node, left=True):
        """It performs fusion between adjacent nodes in order to resolve underflow conditions"""
        # if left == True s is at left of w
        w = tree_node
        s = tree_fusion_node
        u = w._parent
        p_parent = w._list_parent._node._parent #if left else w._list_parent._node._parent

        tree = RedBlackTreeMap()
        p = tree.add(p_parent.key())    # To obtain a position of a generic RBTree
        if left:
            w.tree().catenate(w._tree, p, left=False, T2=s._tree)

            w.tree()._l.fusion(s._tree._l, right=True)
            root = w.tree().root()
            left = w.tree().left(root)
            right = w.tree().right(root)
            w.tree()._update_black_height(left if left is not None else right)

            self.check_overflow(w)

        else:
            s.tree().catenate(s._tree, p, left=True, T2=w._tree)

            s.tree()._l.fusion(w._tree._l, right=False)
            root = s.tree().root()
            left = s.tree().left(root)
            right = s.tree().right(root)
            s.tree()._update_black_height(left if left is not None else right)

            self.check_overflow(s)
            #s.tree().add(p_parent.key())

        del(u.tree()[p.key()])




    def split(self, tree_node):
        """It splits the external B-Tree node, recalling the same internal operation"""
        p = tree_node.tree()._get_median()

        #split operation, called on internal BSTs, returns the obtained subtrees
        if tree_node._parent is None:
            T1, T2 = tree_node.tree().split(p)
        else:
            T1, T2 = tree_node.tree().split(p)

        #parent = tree_node._parent

        #tree_node._parent = tree_node

        #Creo un nuovo albero
        node_left = self.Node(T1)
        node_right = self.Node(T2)


        if tree_node._parent is None:   #Sono la radice
            tree_parent = RedBlackTreeMap()
            np = tree_parent.add(p.key())
            node_parent = self.Node(tree_parent)
            self._root = node_parent
            tree_node._parent = tree_node

            #parent-children references settings
            np._node._left_out._node._child = node_left
            node_left._parent = node_parent
            node_left._list_parent = np._node._left_out

            self._update_children(node_left)

            #parent-children references settings
            np._node._right_out._node._child = node_right
            node_right._parent = node_parent
            node_right._list_parent = np._node._right_out

            self._update_children(node_right)

            self._num_node += 2

            #parent._child = node_parent
        else:
            node_parent = tree_node._parent
            new_p = node_parent.tree().add(p.key())

            #parent-children references settings
            new_p._node._left_out._node._child = node_left
            node_left._parent = node_parent
            node_left._list_parent = new_p._node._left_out

            self._update_children(node_left)

            #parent-children references settings
            new_p._node._right_out._node._child = node_right
            node_right._parent = node_parent
            node_right._list_parent = new_p._node._right_out

            self._update_children(node_right)


            self._num_node += 1
            self.check_overflow(node_parent)



    def _update_children(self, node):
        """Parent attribute updating for node children"""
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
        for elem in tree_node.positions():
            yield elem

    def __len__(self):
        return self._size

    def BFS(self):
        i=0
        if self._num_node ==1:
            root = self._root
            print("\nNODE 0\n")
            print("Size of Node: ", len(root.tree()))
            print("# of children: ", len(root.tree()._l))
            print("RADIX ELEMENTS:")
            for pos in root.positions():
                yield(pos)
        elif not self.is_empty() and self._num_node>1:
            fringe = ArrayQueue()  # known positions not yet yielded
            fringe.enqueue(self.root())  # starting with the root
            while not fringe.is_empty():
                tree_node = fringe.dequeue()  # remove from front of the queue
                if tree_node is not None:
                    print("\nNODO ",i,": \n")
                    print("Size of Node: ", len(tree_node.tree()))
                    print("# of children: ", len(tree_node.tree()._l))
                    print("\nSTRUCTURE: \n")
                    print(tree_node.tree())
                    print("\nELEMENTS: \n")
                    for node in self.bfs(tree_node):  # report this position
                        yield node
                    i+=1

                    for c in tree_node.children():
                        fringe.enqueue(c._node._child)  # add children to back of queue


    def print_tree(self):
        print("\n")
        print("="*30, " BTREE ", "="*30)
        print("\n")
        print("# Elements: ", self._size)
        print("# Node: ", self._num_node)
        print("\n")
        for child in self.BFS():
            print(child, "   BH: ", child._node._black_height, "RED\t" if child._node._red else "BLACK",
                   " parent: ", child._container.parent(child),
                  "\tparent left: " if child._container.parent(
                    child) is not None else "", child._container.parent(child)._node._left == child._node if child._container.parent(
                    child) is not None else "", sep="\t")

        print("\n")
        print("="*30, "", "="*30)
        print("\n")

