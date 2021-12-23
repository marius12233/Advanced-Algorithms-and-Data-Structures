"""Heap Waiting Line Class"""
from .waiting_line_base import WaitingLineBase

class Empty(Exception): #empty exception
  pass


class HeapWaitingLine(WaitingLineBase): # base class defines Job
  """A min-oriented priority queue implemented with a binary heap."""

  #------------------------------ nonpublic behaviors ------------------------------
  def _parent(self, j):
    return (j-1) // 2

  def _left(self, j):
    return 2*j + 1

  def _right(self, j):
    return 2*j + 2

  def _has_left(self, j):
    return self._left(j) < len(self._data)     # index beyond end of list?

  def _has_right(self, j):
    return self._right(j) < len(self._data)    # index beyond end of list?

  def _swap(self, i, j):
    """Swap the elements at indices i and j of array."""
    self._data[i], self._data[j] = self._data[j], self._data[i]

  def _upheap(self, j):
    parent = self._parent(j)
    if j > 0 and self._data[j] < self._data[parent]:
      self._swap(j, parent)
      self._upheap(parent)             # recur at position of parent

  def _downheap(self, j):
    if self._has_left(j):
      left = self._left(j)
      small_child = left               # although right may be smaller
      if self._has_right(j):
        right = self._right(j)
        if self._data[right] < self._data[left]:
          small_child = right
      if self._data[small_child] < self._data[j]:
        self._swap(j, small_child)
        self._downheap(small_child)    # recur at position of small child

  #------------------------------ public behaviors ------------------------------
  def __init__(self):
    """Create a new empty Priority Queue."""
    self._data = []

  def __len__(self):
    """Return the number of items in the priority queue."""
    return len(self._data)

  def add(self, priority, name, lenght, waiting_time):
    """Add a key-value pair to the priority queue."""
    self._data.append(self._Job(priority, name, lenght, waiting_time))
    self._upheap(len(self._data) - 1)            # upheap newly added position

  def min(self):
    """Return but do not remove (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    job = self._data[0]
    return (job._priority, job._name, job._lenght, job._waiting_time)

  def remove_min(self):
    """Remove and return a job with minimum priority.

    Raise Empty exception if empty.
    """
    if self.is_empty():

      raise Empty('Priority queue is empty.')
    self._swap(0, len(self._data) - 1)           # put minimum job at the end
    job = self._data.pop()                      # and remove it from the list;
    self._downheap(0)                            # then fix new root
    return [job._priority, job._name, job._lenght, job._waiting_time]

