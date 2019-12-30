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

from .binary_tree import BinaryTree
from AADS.TdP_collections.list.positional_list import PositionalList


class LinkedBinaryTree(BinaryTree):
  """Linked representation of a binary alberi structure."""


  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a node."""
    __slots__ = '_element', '_parent', '_left', '_right', '_left_out', '_right_out', '_child' # streamline memory usage

    def __init__(self, element, parent=None, left=None, right=None, left_out=None, right_out=None):
      self._element = element
      self._parent = parent
      self._left = left
      self._right = right
      self._left_out = left_out
      self._right_out = right_out
      #self._child = None


  #-------------------------- nested Position class --------------------------
  class Position(BinaryTree.Position):
    """An abstraction representing the location of a single element."""

    def __init__(self, container, node):
      """Constructor should not be invoked by user."""
      self._container = container
      self._node = node

    def element(self):
      """Return the element stored at this Position."""
      return self._node._element

    def __eq__(self, other):
      """Return True if other is a Position representing the same location."""
      return type(other) is type(self) and other._node is self._node

  #------------------------------- utility methods -------------------------------
  def _validate(self, p):
    """Return associated node, if position is valid."""
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
#      raise ValueError('p does not belong to this container')
      pass
    if p._node._parent is p._node:      # convention for deprecated nodes
      raise ValueError('p is no longer valid')
    return p._node

  def _make_position(self, node):
    """Return Position instance for given node (or None if no node)."""
    return self.Position(self, node) if node is not None else None

  #-------------------------- binary alberi constructor --------------------------
  def __init__(self, list_child):
    """Create an initially empty binary alberi."""
    self._root = None
    self._size = 0
    self._l = list_child if list_child is not None else PositionalList()

  #-------------------------- public accessors --------------------------
  def __len__(self):
    """Return the total number of elements in the alberi."""
    return self._size

  def root(self):
    """Return the root Position of the alberi (or None if alberi is empty)."""
    return self._make_position(self._root)

  def parent(self, p):
    """Return the Position of p's parent (or None if p is root)."""
    node = self._validate(p)
    return self._make_position(node._parent)

  def left(self, p):
    """Return the Position of p's left child (or None if no left child)."""
    node = self._validate(p)
    return self._make_position(node._left)

  def right(self, p):
    """Return the Position of p's right child (or None if no right child)."""
    node = self._validate(p)
    return self._make_position(node._right)

  def left_out(self, p):
    node = self._validate(p)
    return node._left_out

  def right_out(self, p):
    node = self._validate(p)
    return node._right_out

  def set_left_out(self,p , left_out):
    node = self._validate(p)
    node._left_out = left_out

  def set_right_out(self, p, right_out):
    node = self._validate(p)
    node._right_out = right_out


  def num_children(self, p):
    """Return the number of children of Position p."""
    node = self._validate(p)
    count = 0
    if node._left is not None:     # left child exists
      count += 1
    if node._right is not None:    # right child exists
      count += 1
    return count

  #-------------------------- nonpublic mutators --------------------------
  def _add_root(self, e, left_out=None, right_out=None):
    """Place element e at the root of an empty alberi and return new Position.

    Raise ValueError if alberi nonempty.
    """
    if self._root is not None:
      raise ValueError('Root exists')
    self._size = 1
    self._root = self._Node(e, left_out=left_out, right_out=right_out)
    return self._make_position(self._root)

  def _add_left(self, p, e, left_out=None):
    """Create a new left child for Position p, storing element e.

    Return the Position of new node.
    Raise ValueError if Position p is invalid or p already has a left child.
    """
    node = self._validate(p)
    if node._left is not None:
      raise ValueError('Left child exists')
    self._size += 1
    node._left = self._Node(e, node, right_out = node._left_out)                  # node is its parent
    child=node._left
    #Remove the left_out ref of the parent
    node._left_out=None
    child._left_out=left_out
    return self._make_position(node._left)

  def _add_right(self, p, e, right_out=None):
    """Create a new right child for Position p, storing element e.

    Return the Position of new node.
    Raise ValueError if Position p is invalid or p already has a right child.
    """
    node = self._validate(p)
    if node._right is not None:
      raise ValueError('Right child exists')
    self._size += 1
    #Il right_out del padre diventa il left_out del nuovo figlio
    node._right = self._Node(e, node, left_out = node._right_out)                 # node is its parent
    node._right_out=None
    child = node._right
    # Aggiorniamo il right out del figlio con il nuovo elemento nella lista
    child._right_out = right_out
    return self._make_position(node._right)

  def _replace(self, p, e):
    """Replace the element at position p with e, and return old element."""
    node = self._validate(p)
    old = node._element
    node._element = e
    return old

  def _delete(self, p, left=True):
    """Delete the node at Position p, and replace it with its child, if any.

    Return the element that had been stored at Position p.
    Raise ValueError if Position p is invalid or p has two children.
    """
    node = self._validate(p)
    if self.num_children(p) == 2:
      raise ValueError('Position has two children')
    child = node._left if node._left else node._right  # might be None
    if child is not None:
      child._parent = node._parent   # child's grandparent becomes parent
    if node is self._root:
      self._root = child             # child becomes root
      child_out = node._left_out if node._left_out else node._right_out
      self._l.delete(child_out)
      child_out = None

    else:
      parent = node._parent

      if left:
        self._l.delete(node._left_out)
        node._left_out = None
      else:
        self._l.delete(node._right_out)
        node._right_out = None


      print("Node to delete: ",node._element._key)
      print("Parent of node to delete: ", parent)

      if node is parent._left:
        if child is None:                       # Il nodo da eliminare è una foglia ed è figlio sx
          if left:
            right_child_out = node._right_out
            parent._left_out=right_child_out
            right_child_out._node._parent=self._make_position(parent)
          else:
            left_child_out = node._left_out
            parent._left_out=left_child_out
            left_child_out._node._parent=self._make_position(parent)

        else:
          child_out = node._left_out if node._left_out else node._right_out
          self._l.delete(child_out)
          child_out = None

        parent._left = child
      else:
        if child is None:
          if left:
            right_child_out = node._right_out
            parent._right_out = right_child_out
            right_child_out._node._parent = self._make_position(parent)
          else:
            left_child_out = node._left_out
            parent._right_out = left_child_out
            left_child_out._node._parent = self._make_position(parent)

        else:
          child_out = node._left_out if node._left_out else node._right_out
          self._l.delete(child_out)
          child_out = None

        parent._right = child


    self._size -= 1
    self._l._computeMedianRemove(p)
    node._parent = node              # convention for deprecated node

    return node._element

  def _attach(self, p, t1, t2):
    """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

    As a side effect, set t1 and t2 to empty.
    Raise TypeError if trees t1 and t2 do not match type of this alberi.
    Raise ValueError if Position p is invalid or not external.
    """
    node = self._validate(p)
    if not self.is_leaf(p):
      raise ValueError('position must be leaf')
    if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type
      raise TypeError('Tree types must match')
    self._size += len(t1) + len(t2)
    if not t1.is_empty():         # attached t1 as left subtree of node
      t1._root._parent = node
      node._left = t1._root
      t1._root = None             # set t1 instance to empty
      t1._size = 0
    if not t2.is_empty():         # attached t2 as right subtree of node
      t2._root._parent = node
      node._right = t2._root
      t2._root = None             # set t2 instance to empty
      t2._size = 0
