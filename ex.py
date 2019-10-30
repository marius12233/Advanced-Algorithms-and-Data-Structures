from list import PositionalList

class CircularPositionalList(PositionalList):

    def __init__(self):
        super().__init__()
        self._count_not_sorted = 0

    class _Node:

        def __init__(self, element, prev, next):
            super().__init__(self, element, prev, next)
            self._sorted_left = True
            self._sorted_right = True


    def before(self, p):
        p = super().before(p)
        node = self._validate(p)
        if node is self._header:
            return node._prev
        return p

    def after(self, p):
        p = super().after(p)
        if p is None:
            return p
        node = self._validate(p)
        if node is self._trailer:
            return node._next
        return p

    def is_empty(self):
        return self._size==0


    def is_sorted(self):
        return self._count_not_sorted==0


    def add_first(self, e):
        p = super().add_first()
        node = self._validate(p)
        self._trailer._next = node
        if self._size == 1:
            self._header._prev = node
        else:
            """if node._element < node._prev._element:
                node._sorted_left = False
                node._prev._sorted_right = False
                self._count_not_sorted += 2"""

            if node._element > node._next._element:
                node._sorted_right = False
                node._next._sorted_left = False
                self._count_not_sorted += 2




if __name__ == "__main__":
    l = CircularPositionalList()
    l.add_first(0)
    print(l.first())



