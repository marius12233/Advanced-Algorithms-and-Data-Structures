import unittest
from circular_positional_list import CircularPositionalList


class TestCircularPositionalList(unittest.TestCase):

    def setUp(self):
        self._l = CircularPositionalList()

    def test_add_first(self):
        e = 10
        #Singolo inserimento
        self._l.add_first(e)
        self.assertEqual(self._l.first().element(),e)
        self.assertEqual(self._l._count_not_sorted,0)

    def test_add_last(self):
        e = 5
        #Singolo inserimento
        self._l.add_last(e)
        self.assertEqual(self._l.last().element(),e)
        self.assertTrue(self._l.is_sorted())

    def test_delete(self):
        self._l.add_last(8)
        self._l.add_last(9)
        self._l.add_last(11)
        e = self._l.delete(self._l.last())
        self.assertEqual(e,11)
        self.assertTrue(self._l.is_sorted())

