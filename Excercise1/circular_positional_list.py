from TdP_collections.list.positional_list import PositionalList

class CircularPositionalList(PositionalList):

    def __init__(self):
        super().__init__()
        #Conta gli elementi non ordinati
        self._count_not_sorted = 0

    class _Node(PositionalList._Node):

        def __init__(self, element, prev, next):
            super().__init__(element, prev, next)
            self._sorted_left = True
            self._sorted_right = True


    def before(self, p):
        node = self._validate(p)
        if node is self._header:
            return self._make_position(node._prev)
        return p

    def after(self, p):
        node = self._validate(p)
        if node is self._trailer:
            return self._make_position(node._next)
        return p

    def is_empty(self):
        return self._size==0


    def is_sorted(self):
        return self._count_not_sorted==0


    def add_first(self, e):
        p = super().add_first(e)
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


    def add_last(self, e):
        p = super().add_last(e)
        node = self._validate(p)
        self._header._prev = node
        if self._size == 1:
            self._trailer._next = node
        else:
            if node._element < node._prev._element:
                node._sorted_left = False
                node._prev._sorted_right = False
                self._count_not_sorted += 2


    def delete(self, p):
        p_prev = self.before(p)
        if p_prev is not None:
            node_prev = self._validate(p_prev)
        p_next = self.after(p)
        if p_next is not None:
            node_next = self._validate(p_next)
        node = self._validate(p)
        el = node._element
        super().delete(p)

        if node._sorted_left == False:
            self._count_not_sorted -= 1
        if node._sorted_right == False:
            self._count_not_sorted -= 1

        #Check i nodi rimasti
        #Verifico il caso in cui elimino un elemento in mezzo
        if node_prev is not self._header:

            if node_prev._next is not None:
                if node_prev._element > node_prev._next._element:
                    if node_prev._sorted_right:
                        node_prev._sorted_right = False
                        self._count_not_sorted += 1
            else:
                if not node_prev._sorted_right:
                    node_prev._sorted_right = True
                    self._count_not_sorted -= 1




        if node_next is not self._trailer:

            if node_next._prev is not None: #Il nodo cancellato non era in testa
                if node_next._element < node_next._prev._element:
                    if node_next._sorted_left:
                        node_prev._sorted_left = False
                        self._count_not_sorted += 1

            else: #Il nodo cancellato era in testa
                if not node_next._sorted_left:
                    node_next._sorted_left = True
                    self._count_not_sorted -= 1

        return el


if __name__ == "__main__":
    l = CircularPositionalList()
    l.add_first(10)
    l.add_last(8)
    l.add_first(7)
    l.add_last(6)
    print(l.delete(l.last()))
    print(l.first().element())
    print(l.last().element())
    print(l.is_sorted())
    print(l._count_not_sorted)


