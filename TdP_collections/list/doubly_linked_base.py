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

class _DoublyLinkedBase:
  """A base class providing a doubly linked list representation."""

  #-------------------------- nested _Node class --------------------------
  # nested _Node class
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = '_element', '_prev', '_next', '_parent', '_child'         # streamline memory

    def __init__(self, element, prev, next, parent=None):            # initialize node's fields
      self._element = element                           # user's element
      self._prev = prev                                 # previous node reference
      self._next = next                                 # next node reference
      self._parent = parent
      self._child = None

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty list."""
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer                  # trailer is after header
    self._trailer._prev = self._header                  # header is before trailer
    self._size = 0                                      # number of elements
    self._median=None                                   # median element
    self._medianKey=None                                # key of the median parent

  #-------------------------- public accessors --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0

  #-------------------------- nonpublic utilities --------------------------

  def _computeMedianAdd(self,nodeParent,newest):
    """It computes the median updating, in case of add operation in the list"""
    if(nodeParent!=None):
      print("nodeparent.key iniziale")
      print(nodeParent.key())


    if (self._size==1): #no operations
      pass
    else:
      if(self._size==2): #first median update, done for the list median (taken for excess)
          print("lunghezza = 2")
          self._median=newest #primo settaggio del mediano
          self._medianKey=nodeParent.key()
          #self._median._parent=nodeParent
          print("il mediano è:")
          print(nodeParent.key())

      else:
          print(self._median._parent.key())
          print(nodeParent.key())
          print("len: ", self._size)
          if(self._medianKey>nodeParent.key() and self._size%2!=0):
            #first update case: key added on the left and odd number of elements for the list
            print("AGGIORNAMENTO LUNGHEZZA DISPARI, AGGIUNTA A SX")
            oldMedian=self._median
            #if(oldMedian._parent._element>newest._element):
            self._median=oldMedian._prev #median moved on the left
            self._medianKey=oldMedian._prev._parent.key()
            #self._median._parent=oldMedian._prev._parent


          if(self._size%2==0 and self._medianKey<nodeParent.key()):
            #second update case: key added on the right and even number of elements for the list
            print("AGGIORNAMENTO LUNGHEZZA PARI, AGGIUNTA A DESTRA!")
            oldMedian=self._median
            self._median=oldMedian._next #median moved on the right
            self._medianKey=oldMedian._next._parent.key()
            #self._median._parent=oldMedian._next._parent

          else:
            #median key setting
            self._medianKey=self._median._parent.key()



  def _computeMedianRemove(self,nodeParent):
    """It computes the median updating, in case of remove operation in the list"""
    if(nodeParent!=None):
      print("nodeparent.key iniziale")
      print(nodeParent.key())

    if (self._size==1): #no operations
      pass
    else:
      if(self._size==2): #None setting for the median, in case of all the list elements remove
          print("lunghezza = 2")
          self._median=None #eliminazione del mediano=root
          self._medianKey=None
          #self._median._parent=nodeParent
          print("il mediano è:")
          print(nodeParent.key())

      else:
          #print(self._median._parent.key())
          print(self._medianKey)
          print(nodeParent.key())
          print(self.__len__())
          if(self._medianKey<nodeParent.key() and self.__len__()%2==0):
            #first update case: key removed from the right and even number of elements for the list
            print("AGGIORNAMENTO LUNGHEZZA DISPARI, AGGIUNTA A SX")
            oldMedian=self._median
            #if(oldMedian._parent._element>newest._element):
            self._median=oldMedian._prev #median moved on the left
            self._medianKey=oldMedian._prev._parent.key()
            #self._median._parent=oldMedian._prev._parent


          if(self._size%2!=0 and self._medianKey>nodeParent.key()):
            #second update case: key removed on the left and odd number of elements for the list
            print("AGGIORNAMENTO LUNGHEZZA PARI, AGGIUNTA A DESTRA!")
            oldMedian=self._median
            self._median=oldMedian._next #median moved on the right
            self._medianKey=oldMedian._next._parent.key()
            #self._median._parent=oldMedian._next._parent

        #The following cases regarde median deletions:
          if(self._size%2==0 and self._median._parent.key()==nodeParent.key()):
            #even number of elements for the list
            oldMedian=self._median
            self._median=oldMedian._next #median moved on the right
            self._medianKey=oldMedian._next._parent.key()
          if(self.__len__()%2!=0 and self._median._parent.key()==nodeParent.key()):
            #odd number of elements for the list
            oldMedian=self._median
            self._median=oldMedian._prev  #median moved on the left
            self._medianKey=oldMedian._prev._parent.key()

  def _getMedian(self):
    return self._median

  def _getKeyMedian(self):
    return self._medianKey

  def _insert_between(self, e, predecessor, successor,nodeParent): #nodeParent da cancellare
    """Add element e between two existing nodes and return new node."""
    newest = self._Node(e, predecessor, successor)      # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element                             # record deleted element
    node._prev = node._next = node._element = None      # deprecate node
    return element                                      # return deleted element

