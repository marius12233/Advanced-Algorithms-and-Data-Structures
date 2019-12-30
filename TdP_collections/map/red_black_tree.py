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
    print("Called on ", p.key())
    p = self.parent(p)
    while p is not None:
        delta_black_height = 0 if p._node._red else 1
        left_black_height = self.left(p)._node._black_height if self.left(p) is not None else 1
        right_black_height = self.right(p)._node._black_height if self.right(p) is not None else 1
        p._node._black_height = max( left_black_height, right_black_height) + delta_black_height
        p = self.parent(p)


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
    if not self._is_red(y): # y is black; will apply Case 1 or 2
      x = self._get_red_child(y)
      if x is not None: # Case 1: y is black and has red child x; do "transfer"
        old_color = self._is_red(z)
        middle = self._restructure(x)
        self._set_color(middle, old_color)   # middle gets old color of z
        self._set_black(self.left(middle))   # children become black
        self._set_black(self.right(middle))
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

  def catenate(self, T, pivot, left=True, T2=None):
    if T2 is None:
        p = T.add(pivot.key())

        if left:
          p._node._right_out = pivot._node._right_out
        else:
          p._node._left_out = pivot._node._left_out
    else:
        pivot._node._left_out = None
        pivot._node._right_out = None
        root =  T2.root()
        black_height = root._node._black_height
        p = self._find_black_height(T, black_height=black_height, left=left)
        #nel caso in cui la black height uguale a black_height è maggiore o il nodo è rosso
        #significa che il nodo che dobbiamo rendere fratello della root di T2 è una foglia, quindi None
        if(p._node._black_height > black_height or p._node._red):
            raise NotImplementedError("Not yet implemented")
        else:
            parent = T.parent(p)
            if left:
                self._attach_left(p, parent, pivot, root, T)
            else:
                self._attach_right(p, parent, pivot, root, T)



  def _attach_left(self, p, parent, pivot, root, T):
      print("In attach left")
      print(p.key())
      print(parent)
      print(root.key())
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
      print("In attach right")
      print(p.key())
      print(parent)
      print(root.key())
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


  def split(self, p):

    T1 = RedBlackTreeMap(self._l)
    T2 = RedBlackTreeMap(self._l)

    if self.is_root(p):
      T1._root = self.left(p)._node
      T1._root._parent = None
      T1._set_black(T1.root())
      T1._size = self._size//2

      T2._root = self.right(p)._node
      T2._root._parent = None
      T2._set_black(T2.root())
      T2._size = self._size//2

    else:

      predecessor = self.before(p)
      successor = self.after(p)
      parent = self.parent(p)

      # Unlink the parent of the median from the median child

      if p == self.left(parent):
        parent._node._left = None
      else:
        parent._node._right = None

      p._node._left = None
      p._node._right = None
      p._node._parent = p
      T1._size = ((self._size//2) if self.is_root(predecessor) else (self._size//2 -1))

      root1 = self.left(predecessor)._node
      #predecessor._node._right_out = p._node._left_out
      T1._root = root1
      T1._root._parent = None
      T1._root._red = False
      #T1._set_black(T1.root())
      self.catenate(T1, predecessor, left=True)


      T2._size = ((self._size//2) if self.is_root(successor) else (self._size//2 -1))
      root2 = self.right(successor)._node
      #successor._node._left_out = p._node._right_out
      T2._root = root2
      T2._root._parent = None
      T2._root._red = False
      self.catenate(T2, successor, left=False)

    return (T1, T2)

#questo metodo restituisce il mediano dell'albero
  def _get_median(self):
    listmedian=self._l._median
    #condizione in cui il mediano dell'albero è proprio la root
    if len(self)%2==0 and listmedian._parent!=listmedian._prev._parent:
      return self.root()
    else:
        return listmedian._parent
