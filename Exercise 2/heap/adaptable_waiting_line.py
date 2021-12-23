"""Adaptable Heap Waiting Line Class"""
from .heap_waiting_line import HeapWaitingLine

class AdaptableHeapWaitingLine(HeapWaitingLine):
  """A locator-based priority queue implemented with a binary heap."""

  #------------------------------ nested Locator class ------------------------------
  class Locator(HeapWaitingLine._Job):
    """Token for locating an entry of the priority queue."""
    __slots__ = '_index'                 # add index as additional field

    def __init__(self, p, n, l, j):
      super().__init__(p, n, l, 0)
      self._index = j

  #------------------------------ nonpublic behaviors ------------------------------
  # override swap to record new indices
  def _swap(self, i, j):
    super()._swap(i,j)                   # perform the swap
    self._data[i]._index = i             # reset locator index (post-swap)
    self._data[j]._index = j             # reset locator index (post-swap)

  def _bubble(self, j):
    if j > 0 and self._data[j] < self._data[self._parent(j)]:
      self._upheap(j)
    else:
      self._downheap(j)

  #------------------------------ public behaviors ------------------------------
  def add(self, priority, name, lenght):
    """Add a new job with his properties."""
    token = self.Locator(priority, name, lenght, len(self._data)) # initiaize locator index
    self._data.append(token)
    self._upheap(len(self._data) - 1)
    return token

  def update(self, loc, priority, name, lenght):
    """Update the properties for the entry identified by Locator loc."""
    j = loc._index
    if not (0 <= j < len(self) and self._data[j] is loc):
      raise ValueError('Invalid locator')
    loc._priority = priority
    loc._name = name
    loc._lenght=lenght
    self._bubble(j)

  def reset(self):
    """Update some properties (in particular priority and waiting time) for every job of the waiting line."""
    for i in range(0,len(self._data)):
        self._data[i]._waiting_time=0
        if self._data[i]._priority > -20:
            self._data[i]._priority = self._data[i]._priority -1


  def remove(self, loc):
    """Remove and return the (p,n,l) pair identified by Locator loc."""
    j = loc._index
    if not (0 <= j < len(self) and self._data[j] is loc):
      raise ValueError('Invalid locator')
    if j == len(self) - 1:                # job at last position
      self._data.pop()                    # just remove it
    else:
      self._swap(j, len(self)-1)          # swap job to the last position
      self._data.pop()                    # remove it from the list
      self._bubble(j)                     # fix item displaced by the swap
    return [loc._priority, loc._name, loc._lenght]


