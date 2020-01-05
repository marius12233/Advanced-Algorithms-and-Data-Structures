# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .binary_search_tree import TreeMap

class RedBlackTreeMap(TreeMap):
  """Sorted map implementation using a red-black tree."""

  #-------------------------- nested _Node class --------------------------
  class _Node(TreeMap._Node):
    """Node class for red-black tree maintains bit that denotes color."""
    __slots__ = '_red', '_black_height'     # add additional data member to the Node class

    def __init__(self, element, parent=None, left=None, right=None, left_out=None, right_out=None):
      super().__init__(element, parent, left, right, left_out, right_out)
      self._red = True     # new node red by default
      self._black_height=1 # new node has black children, so its black height is initially 1

      # we maintain black height to perform alghorithms of split and catenate efficiently

  #------------------------- positional-based utility methods -------------------------
  # we consider a nonexistent child to be trivially black
  def _set_red(self, p):
      if p is None:
          return

      if p._node._red == False:
          p._node._black_height-=1
          self._update_black_height(p)
      p._node._red = True
  def _set_black(self, p):
      if p is None:
          return
      if p._node._red==True:
          p._node._black_height += 1
          self._update_black_height(p)
      p._node._red = False

  def _set_color(self, p, make_red): p._node._red = make_red
  def _is_red(self, p): return p is not None and p._node._red
  def _is_red_leaf(self, p): return self._is_red(p) and self.is_leaf(p)

  def _get_red_child(self, p):
    """Return a red child of p (or None if no such child)."""
    for child in (self.left(p), self.right(p)):
      if self._is_red(child):
        return child
    return None

  #------------------------- support for insertions -------------------------

  def _update_black_height(self, p):
    """
    :param p: The node to start to update black height
ì    """
    parent = self.parent(p)
    while parent is not None:
        delta_black_height = 0 if parent._node._red else 1
        left_black_height = self.left(parent)._node._black_height if self.left(parent) is not None else 1
        right_black_height = self.right(parent)._node._black_height if self.right(parent) is not None else 1
        parent._node._black_height = max( left_black_height, right_black_height) + delta_black_height
        parent = self.parent(parent)

  def _rebalance_access(self, p):
      self._update_black_height(p)


  def _rebalance_insert(self, p):
    self._resolve_red(p)                         # new node is always red
    #self._update_black_height(p)

  def _resolve_red(self, p):
    if self.is_root(p):
      self._set_black(p)                         # make root black
    else:
      parent = self.parent(p)
      if self._is_red(parent):                   # double red problem
        uncle = self.sibling(parent)
        if not self._is_red(uncle):              # Case 1: misshapen 4-node
          middle = self._restructure(p)          # do trinode restructuring
          self._set_black(middle)                # and then fix colors
          self._set_red(self.left(middle))
          self._set_red(self.right(middle))

        else:                                    # Case 2: overfull 5-node
          grand = self.parent(parent)
          self._set_red(grand)                   # grandparent becomes red
          self._set_black(self.left(grand))      # its children become black
          self._set_black(self.right(grand))
          self._resolve_red(grand)               # recur at red grandparent
      else:
          self._update_black_height(p)


  #------------------------- support for deletions -------------------------


  def _rebalance_delete(self, p):
    print("REBALANCE DELETE CALLING::::")
    if len(self) == 1:
      self._set_black(self.root())  # special case: ensure that root is black
    elif p is not None:
      n = self.num_children(p)
      if n == 1:                    # deficit exists unless child is a red leaf
        c = next(self.children(p))
        if not self._is_red_leaf(c):
          self._fix_deficit(p, c)
      elif n == 2:                  # removed black node with red child
        if self._is_red_leaf(self.left(p)):
          self._set_black(self.left(p))

        else:
          self._set_black(self.right(p))

  def _fix_deficit(self, z, y):
    """Resolve black deficit at z, where y is the root of z's heavier subtree."""
    print("\n\nFIX DEFICIT::::::\n\n")
    if not self._is_red(y): # y is black; will apply Case 1 or 2
      x = self._get_red_child(y)
      if x is not None: # Case 1: y is black and has red child x; do "transfer"
        old_color = self._is_red(z)
        middle = self._restructure(x)
        self._set_color(middle, old_color)   # middle gets old color of z
        self._set_black(self.left(middle))   # children become black
        self._set_black(self.right(middle))
        #black height of y does not change, but change that of x and z
        z._node._black_height=x._node._black_height
        self._update_black_height(self.left(middle))

      else: # Case 2: y is black, but no red children; recolor as "fusion"
        self._set_red(y)
        if self._is_red(z):
          self._set_black(z)                 # this resolves the problem
        elif not self.is_root(z):
          self._fix_deficit(self.parent(z), self.sibling(z)) # recur upward
    else: # Case 3: y is red; rotate misaligned 3-node and repeat
      self._rotate(y)
      self._set_black(y)
      self._set_red(z)
      if z == self.right(y):
        self._fix_deficit(z, self.left(z))
      else:
        self._fix_deficit(z, self.right(z))

  def _node_catenate(self, p):
      parent = self._subtree_search(self.root(), p.key())

      if parent.key() > p.key():
          parent._node._left = p._node

      else:
          parent._node._right = p._node
      p._node._parent = parent._node

      self._set_red(p)
      return p

  def catenate(self, T, pivot, left=True, T2=None):
    """
    With this method we want to concatenate 2 tree T1 and T2, or just a node pivot to a T tree

    :param T: The tree at wich attach the other objects
    :param pivot: The pivot of the operation. It needs to catenate the 2 structures
    :param left: If we want to attach T2 at left or at right of T1
    :param T2: The second structure to attach. If it is None, we attach only puvot at T1
    """


    # print(T.left(T.right(T.root())))
    # print(T.right(T.root()))

    if T2 is None:
        p = T._node_catenate(pivot) #T.add(pivot.key())

        print("After concatenate")
        print(T.root())
        print(T.left(T.root()))
        print(T.right(T.root()))
        print(T.left(T.right(T.root())))
        print(T.right(T.right(T.root())))
        print(T.left(T.left(T.root())))
        print(T.right(T.left(T.root())))



        #print(T.right(T.right(T.right(T.root()))))


        # If the node is red but has sibling black, re-color sibling as black to decrease black height
        sibling = self.sibling(p)
        if p._node._red and not sibling._node._red:
            self._set_red(sibling)

    else:
        pivot._node._left_out = None
        pivot._node._right_out = None
        root =  T2.root()
        black_height = root._node._black_height
        # In accord to the alghorithm for concatenating 2 RBTree T1 and T2, we have to find in the T1 three a blakc node
        # with black height equal to the black height of the root of T2
        p = self._find_black_height(T, black_height=black_height, left=left)

        #nel caso in cui la black height uguale a black_height è maggiore o il nodo è rosso
        #significa che il nodo che dobbiamo rendere fratello della root di T2 è una foglia, quindi None
        if(p._node._black_height > black_height or p._node._red):
            raise NotImplementedError("Not yet implemented")
        else:
            parent = T.parent(p)
            if left:    # Concatenate T2 at left of T1
                self._attach_left(p, parent, pivot, root, T)
            else:
                self._attach_right(p, parent, pivot, root, T)



  def _attach_left(self, p, parent, pivot, root, T):
      """
      :param p: The node in T1 that has the same black height of the radix of T2
      :param parent:
      :param pivot: The node used to attach the 2 trees
      :param root: The root of T2 tree
      :param T: the tree at wich attach T2
      :return:
      """
      pivot._node._left = root._node
      pivot._node._right = p._node
      root._node._parent = pivot._node
      p._node._parent = pivot._node
      if parent is None:
          T._root = pivot._node
          pivot._node._parent = None
          pivot._node._red = False
          pivot._node._black_height = max(T.left(pivot)._node._black_height, T.right(pivot)._node._black_height)
      else:
          pivot._node._parent = parent._node
          parent._node._left = pivot._node
          T._root = parent._node
          parent._node._red = False
          pivot._node._red = True
          T._rebalance_insert(pivot)


  def _attach_right(self, p, parent, pivot, root, T):
      pivot._node._left = p._node
      pivot._node._right = root._node
      root._node._parent = pivot._node
      p._node._parent = pivot._node
      if parent is None:
          T._root = pivot._node
          pivot._node._parent = None
          pivot._node._red=False
          self._update_black_height(p)
          #pivot._node._black_height = max(T.left(pivot)._node._black_height, T.right(pivot)._node._black_height)
      else:
          pivot._node._parent = parent._node
          parent._node._right = pivot._node
          T._root = parent._node
          pivot._node._red = True
          T._rebalance_insert(pivot)


  def _find_black_height(self, T, black_height=1, left=True):
      """
      :param T: Tree in which search for a node with black height black_height
      :param black_height: int
      :param left: parameter to say if search in leftmost or rightmost tree
      :return: position of a node that has black height = black_height
      """
      p = T.root()
      print("Finding black height: ", black_height)

      while p is not None:
        if p._node._black_height == black_height and p._node._red==False:
            return p
        if p._node._black_height < black_height:
            raise ValueError("There is no element with this black height")
        else:
            if left:
                if T.left(p) is None:
                    return p
                p = T.left(p)
            else:
                if T.right(p) is None:
                    return p
                p = T.right(p)


  def split(self, p, split_root=False):
    """
    This method is used to split a RBTree in 2 RBTrees according to a position p
    :param p: The position according to split the tree
    :return T1,T2 : Tuple with the 2 tree obtained from splitting
    """
    print("Before splitting: ")
    for pos in self.breadthfirst():
        print("Key: ", pos.key(), " Black height: ", pos._node._black_height,
              " Parent: ", self.parent(pos).key() if self.parent(pos) is not None else None,
              " Left: ", self.left(pos).key() if self.left(pos) is not None else None ,
              " Right: ", self.right(pos).key() if self.right(pos) is not None else None ,
              " Red: ", pos._node._red,
              " Is root: ", self.is_root(pos),
              " Is median: ", self._l._median._parent)



    print("ORIGINAL LIST BEFORE SPLITTING")
    for pos in  self._l:
        print(pos._node._parent.key())

    l1, l2 = self._l.splitMedian()
    #l = self._l
    T1 = RedBlackTreeMap(l1)
    T2 = RedBlackTreeMap(l2)

    print("======= LIST SPLITTING: =======")
    print("Original LIST: ")
    print("L1")
    print("SIZE: ", len( self._l))
    print("MEDIAN: ", self._l._getMedian()._parent.key())


    print("L1")
    print("SIZE: ", len(l1))
    for pos in l1:
        print(pos._node._parent.key(), " IS MEDIAN: ", pos._node==l1._median)
    print("MEDIAN: ", l1._medianKey)

    print("L2")
    print("SIZE: ", len(l2))
    for pos in l2:
        print(pos._node._parent.key(), " IS MEDIAN: ", pos._node==l2._median)
    print("MEDIAN: ", l2._medianKey)

    print("\n ORIGINAL TREE BEFORE SPLITTING\n")
    for pos in self.positions():
        print(pos.key())

    if self.is_root(p):
      # The simplest case is when p is the root.
      T1._root = self.left(p)._node
      T1._root._parent = None
      T1._set_black(T1.root())
      T1._size = len(l1)-1

      T2._root = self.right(p)._node
      T2._root._parent = None
      T2._set_black(T2.root())
      T2._size = len(l2)-1

    else:

      predecessor = self.before(p)
      successor = self.after(p)
      parent = self.parent(p)


      print("MEDIAN PREDECESSOR E SUCCESSOR: ")
      print(p.key())
      print(predecessor.key())
      print(successor.key())
      root1 = self.before(predecessor)._node
      root2 = self.after(successor)._node




      # Unlink the parent of the median from the median child

      if p == self.left(parent):
        parent._node._left = None
        #parent._node._left_out = p._node._right_out
      else:
        parent._node._right = None
        #parent._node._right_out = p._node._left_out

      if predecessor._node._right_out is None:  # Il predecessor non può avere un figlio destro che non sia il mediano p, altrimenti non sarebbe il predecessor
          predecessor._node._right_out = p._node._left_out
          predecessor._node._right_out._parent = predecessor
      if successor._node._left_out is None:    # Il successor non può avere figlio sinistro che non sia il meiano p, altrimenti non sarebbe il successor
          successor._node._left_out = p._node._right_out
          successor._node._left_out._parent = successor

      # predecessor._node._parent = None
      # successor._node._parent = None
      #
      # root1._parent = None
      # root2._parent = None


      #Unlink the predecessor and successor of the 2 pivot pred and succ
      if root1._parent is not None and not root1._parent == predecessor._node:
          print(" SONO ENTRATO QUIIIIII!!!!!")
          parent = root1._parent
          if root1 == parent._right:
              root1._left = parent
              parent._right_out = root1._left_out
              parent._parent = root1
              parent._right = None
          else:
              root1._right = root1._parent
              parent._left_out = root1._right_out
              parent._parent = root1
              parent._left = None
          root1._parent = None
          root1._black_height, parent._black_height = parent._black_height, root1._black_height
          root1._red, parent._red = parent._red, root1._red


      root1._right = None


      if root2._parent is not None and not root2._parent == predecessor._node:
          print(" SONO ENTRATO QUIIIIII!!!!!")
          parent = root2._parent
          if root2 == parent._right:
              root2._left = parent
              parent._right_out = root2._left_out
              parent._parent = root2
              parent._right = None
          else:
              root2._right = root2._parent
              parent._left_out = root2._right_out
              parent._parent = root2
              parent._left = None
          root2._parent = None
          root2._black_height, parent._black_height = parent._black_height, root1._black_height
          root2._red, parent._red = parent._red, root1._red


      root2._left = None

      predecessor._node._right = None
      predecessor._node._left = None
      successor._node._right=None
      successor._node._left = None

      # Delete median node from the structure
      p._node._left = None
      p._node._right = None
      p._node._parent = p


      T1._size= len(l1) - 1
      T1._root = root1
      T1._root._parent = None
      T1._root._red = False
      #T1._set_black(T1.root())
      self.catenate(T1, predecessor, left=True)  # We catenate the successor at right of T2 tree

      T2._size = len(l2)-1

      T2._root = root2
      T2._root._parent = None
      T2._root._red = False
      self.catenate(T2, successor, left=False)  # We catenate the successor at right of T2 tree

    return (T1, T2)

#questo metodo restituisce il mediano dell'albero
  def _get_median(self):
    listmedian=self._l._median
    print("len lista: ", len(self._l))
    #condizione in cui il mediano dell'albero è proprio la root
    if len(self._l)%2==0 and not listmedian._parent==listmedian._prev._parent:
      print("DIVERSO")
      print(listmedian._parent.key())
      print(listmedian._prev._parent.key())
      if listmedian._prev._parent == self.left(listmedian._parent):
          return listmedian._parent

      return self.before(listmedian._parent)
    else:
        print("MEDIANO: ", listmedian._parent.key())
        print("Prev MEDIAN: ", listmedian._prev._parent.key())
        return listmedian._parent
