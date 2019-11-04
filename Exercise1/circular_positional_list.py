from TdP_collections.list.positional_list import PositionalList

class CircularPositionalList(PositionalList):
    
    #-------------------------- Circular Positional List constructor --------------------------
    def __init__(self):
        super().__init__()
        # Conta gli elementi non ordinati
        self._count_not_sorted = 0
        # Utilizziamo la proprietà is_reversed per indicare che la lista è reversed rispetto alla struttura interna
        self._is_reversed = False
    
    
    #-------------------------- nested _Node class --------------------------
    # override of the nested _Node class in Doubly Linked Base class
    class _Node(PositionalList._Node):

        def __init__(self, element, prev, next):
            super().__init__(element, prev, next)
            self._sorted_left = True
            self._sorted_right = True
    
    
    #-------------------------- utility methods -------------------------------
    def is_empty(self):
        return self._size==0

    def is_sorted(self):
        if self._is_reversed:
            return self._count_not_sorted==(2*self._size-2)
        return self._count_not_sorted==0
    
    
    #-------------------------- accessors methods -------------------------------
    # ## To implement reverse in O(1) is needed to override first and last methods ## #
    def first(self):
        if self._is_reversed:
            self._is_reversed=False
            p = super().last()
            self._is_reversed = True
            return p
        return super().first()

    def last(self):
        if self._is_reversed:
            self._is_reversed = False
            p = super().first()
            self._is_reversed = True
            return p
        return super().last()
    
    # override inherited version to make the inherited Position List circular
    def before(self, p):
        #Se è reversed, il metodo before sarebbe il metodo after
        if self._is_reversed:
            #Dato che ogni metodo controerà se è reversed, per far eseguire after è necessario settare is_reversed a False
            self._is_reversed = False
            p2 = self.after(p)
            self._is_reversed = True
            return p2

        node = self._validate(p)
        before = node._prev
        if before is self._header:
            return self._make_position(before._prev)
        return super().before(p)
    
    # override inherited version to make the inherited Position List circular
    def after(self, p):
        #Se è reversed, il metodo before sarebbe il metodo after
        if self._is_reversed:
            #Dato che ogni metodo controerà se è reversed, per far eseguire after è necessario settare is_reversed a False
            self._is_reversed = False
            p2 = self.before(p)
            self._is_reversed = True
            return p2
        node = self._validate(p)
        next = node._next
        if next is self._trailer:
            return self._make_position(next._next)
        return super().after(p)
    
    
    #--------------------------- mutators methods -------------------------------
    def add_first(self, e):
        if self._is_reversed:
            #Dato che ogni metodo controerà se è reversed, per far eseguire after è necessario settare is_reversed a False
            self._is_reversed = False
            p = self.add_last(e)
            self._is_reversed = True
            return p

        p = super().add_first(e)
        node = self._validate(p)
        self._trailer._next = node
        if self._size == 1:
            self._header._prev = node
        else:
            if node._element > node._next._element:
                node._sorted_right = False
                node._next._sorted_left = False
                self._count_not_sorted += 2
        return p

    def add_last(self, e):
        if self._is_reversed:
            #Dato che ogni metodo controerà se è reversed, per far eseguire after è necessario settare is_reversed a False
            self._is_reversed = False
            p = self.add_first(e)
            self._is_reversed = True
            return p

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
        return p

    def delete(self, p):
        node_prev, node_next = None, None
        p_prev, p_next = None, None

        node = self._validate(p)
        # aggiorno i valori sorted_left e sorted_right
        if node._sorted_left == False:
            self._count_not_sorted -= 1
        if node._sorted_right == False:
            self._count_not_sorted -= 1

        if node._prev is not self._header:
            p_prev = self.before(p)
            node_prev = self._validate(p_prev)
        if node._next is not self._trailer:
            p_next = self.after(p)
            node_next = self._validate(p_next)

        #Poi posso eliminarlo
        el = node._element
        super().delete(p)

        if self.is_empty(): #Nodo da cancellare era l'unico
            return el

        # Check i nodi rimasti
        # Verifico il caso in cui elimino un elemento in mezzo
        if node_prev is not None:  # Se il precedente del nodo eliminato non è header (il nodo da eliminare NON stava in testa)

            if node_prev._next is not self._trailer:  # Il nodo rimasto non è l'ultimo
                if node_prev._element > node_prev._next._element:
                    if node_prev._sorted_right:
                        node_prev._sorted_right = False
                        self._count_not_sorted += 1
            else:  # Il nodo rimasto è nell'ultima position
                self._header._prev = node_prev
                if not node_prev._sorted_right:
                    node_prev._sorted_right = True
                    self._count_not_sorted -= 1

        if node_next is not None:

            if node_next._prev is not self._header: # Il nodo cancellato non era in testa
                if node_next._element < node_next._prev._element:
                    if node_next._sorted_left:
                        node_prev._sorted_left = False
                        self._count_not_sorted += 1

            else: # Il nodo cancellato era in testa (adesso è il next che sta in testa)
                self._trailer._next = node_next
                if not node_next._sorted_left:
                    node_next._sorted_left = True
                    self._count_not_sorted -= 1

        return el

    def add_before(self,p,e):
        if self._is_reversed:
            # Dato che ogni metodo controerà se è reversed, per far eseguire after è necessario settare is_reversed a False
            self._is_reversed = False
            p = self.add_after(p, e)
            self._is_reversed = True
            return p

        node = self._validate(p)
        if node is self._header._next:
            return self.add_first(e)
        predecessor = self.before(p)
        successor = p
        node = self._insert_between_rebalance(e, predecessor, successor)
        return self._make_position(node)

    def add_after(self,p,e):
        if self._is_reversed:
            # Dato che ogni metodo controerà se è reversed, per far eseguire after è necessario settare is_reversed a False
            self._is_reversed = False
            p = self.add_before(p, e)
            self._is_reversed = True
            return p

        node = self._validate(p)
        if node is self._trailer._prev:
            return self.add_last(e)
        predecessor = p
        successor = self.after(p)
        node = self._insert_between_rebalance(e, predecessor, successor)
        return self._make_position(node)

    def _insert_between_rebalance(self, e, predecessor, successor):
        """This method perform the updating of the sorted_right and
           sorted_left properties of the nodes involved in the insert
        """
        node_prev = self._validate(predecessor)
        node_next = self._validate(successor)
        p = super()._insert_between(e,node_prev,node_next)
        node = self._validate(p)

        if e < node_prev._element:
            if node_prev._sorted_right == True:
                node_prev._sorted_right = False
                self._count_not_sorted+=1
            node._sorted_left = False
            self._count_not_sorted += 1

        if e > node_next._element:
            if node_next._sorted_left == True:
                node_next._sorted_left = False
                self._count_not_sorted+=1
            node._sorted_right = False
            self._count_not_sorted += 1

        return node

    def reverse(self):
        self._is_reversed = not self._is_reversed

    def replace(self, p, e):
        old = super().replace(p, e)

        node = self._validate(p)
        if node._prev is not self._header:
            p_prev = self.before(p)
            if p_prev is not None:
                node_prev = self._validate(p_prev)
                if e < node_prev._element:
                    if node_prev._sorted_right == True:
                        node_prev._sorted_right = False
                        self._count_not_sorted+=1
                    if node._sorted_left == True:
                        node._sorted_left = False
                        self._count_not_sorted+=1
                else:
                    if node_prev._sorted_right == False:
                        node_prev._sorted_right = True
                        self._count_not_sorted-=1
                    if node._sorted_left == False:
                        node._sorted_left = True
                        self._count_not_sorted-=1

        if node._next is not self._trailer:
            p_next = self.after(p)
            if p_next is not None:
                node_next = self._validate(p_next)
                if e > node_next._element:
                    if node_next._sorted_left == True:
                        node_next._sorted_left = False
                        self._count_not_sorted+=1
                    if node._sorted_right == True:
                        node._sorted_right = False
                        self._count_not_sorted+=1
                else:
                    if node_next._sorted_left == False:
                        node_next._sorted_left = True
                        self._count_not_sorted-=1
                    if node._sorted_right == False:
                        node._sorted_right = True
                        self._count_not_sorted-=1

        return old
        
    def delete_first(self):
        if self.is_empty() is True:
            raise TypeError('List is empty')
        else:
            first_position = super().first(self)
            first_element = self.delete(first_position)
            return first_element

    def delete_last(self):
        if self.is_empty() is True:
            raise TypeError('List is empty')
        else:
            last_position = super().last(self)
            last_element = self.delete(last_position)
            return last_element

