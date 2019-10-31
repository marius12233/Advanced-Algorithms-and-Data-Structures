import unittest
from circular_positional_list import CircularPositionalList


class TestCircularPositionalList(unittest.TestCase):

    def setUp(self):
        self._l = CircularPositionalList()

    def test_after(self):
        p1 = self._l.add_last(1)
        p2 = self._l.add_last(2)
        p3 = self._l.add_last(3)
        self.assertEqual(self._l.after(self._l.first()).element(), 2)
        self.assertEqual(self._l.after(p2).element(), 3)
        self.assertEqual(self._l.after(p3).element(), 1)

    def test_before(self):
        p1 = self._l.add_last(1)
        p2 = self._l.add_last(2)
        p3 = self._l.add_last(3)
        self.assertEqual(self._l.before(self._l.last()).element(), 2)
        self.assertEqual(self._l.before(p2).element(), 1)
        self.assertEqual(self._l.before(p1).element(), 3)


    def test_add_first(self):
        e = 10
        #Singolo inserimento
        p = self._l.add_first(e)
        self.assertEqual(self._l.first().element(),e)
        self.assertEqual(self._l._count_not_sorted,0)
        self.assertEqual(p.element(), e)

    def test_add_last(self):
        e = 5
        #Singolo inserimento
        p = self._l.add_last(e)
        self.assertEqual(self._l.last().element(),e)
        self.assertTrue(self._l.is_sorted())
        self.assertEqual(p.element(), e)

    def test_add_before(self):
        succ = self._l.add_first(10)
        p = self._l.add_before(succ,9)
        self.assertEqual(self._l.first().element(),p.element())
        self.assertTrue(self._l.is_sorted())
        prev = self._l.add_before(p, 8)
        self.assertEqual(self._l.first().element(), 8)
        self.assertEqual(self._l.after(self._l.first()).element(), 9)

    def test_add_after(self):
        succ = self._l.add_first(9)
        p = self._l.add_after(succ,10)
        self.assertEqual(self._l.last().element(),p.element())
        self.assertTrue(self._l.is_sorted())
        prev = self._l.add_after(p, 11)
        self.assertEqual(self._l.last().element(), 11)
        self.assertEqual(self._l.before(self._l.last()).element(), 10)

    def test_delete(self):
        self._l.add_last(8)
        self._l.add_last(9)
        self._l.add_last(11)
        # 8 -> 9 -> 10
        e = self._l.delete(self._l.last())
        # 8 -> 9
        self.assertEqual(e,11)
        self.assertTrue(self._l.is_sorted())
        e = self._l.delete(self._l.first())
        # 9
        self.assertEqual(e,8)
        self.assertTrue(self._l.is_sorted())

        e = self._l.delete(self._l.first())
        # Vuota
        self.assertEqual(e,9)
        self.assertTrue(self._l.is_sorted())

    def test_reverse(self):
        self._l.add_last(3)
        self._l.add_last(4)
        self._l.add_last(5)
        # 3 -> 4 -> 5
        self._l.reverse()
        # 5 -> 4 -> 3
        self.assertTrue(self._l._is_reversed)
        self.assertEqual(self._l.first().element(), 5)
        self.assertEqual(self._l.last().element(), 3)
        self.assertEqual(self._l.after(self._l.first()).element(), 4)
        self.assertEqual(self._l.before(self._l.last()).element(), 4)
        self.assertFalse(self._l.is_sorted())

        p = self._l.add_last(1)
        # 5 -> 4 -> 3 -> 1
        self.assertEqual(self._l.first().element(), 5)
        self.assertEqual(self._l.last().element(), 1)
        self.assertEqual(self._l.after(self._l.first()).element(), 4)
        self.assertEqual(self._l.before(p).element(), 3)

        p2 = self._l.add_before(p, 2)

        # 5 -> 4 -> 3 -> 2 -> 1
        self.assertEqual(self._l.last().element(), 1)
        self.assertEqual(self._l.before(p2).element(), 3)
        self.assertEqual(self._l.before(self._l.last()).element(), 2)

        self._l.reverse()
        # 1 -> 2 -> 3 -> 4 -> 5
        self.assertFalse(self._l._is_reversed)
        self._l.add_first(0.5)
        self.assertEqual(self._l.first().element(), 0.5)
        self.assertEqual(self._l.last().element(), 5)
        self.assertTrue(self._l.is_sorted())

    def test_is_sorted(self):
        self._l.add_last(10)
        self._l.add_last(9)
        self._l.add_last(8)
        self.assertFalse(self._l.is_sorted())
        self._l.reverse()
        self.assertTrue(self._l.is_sorted())



