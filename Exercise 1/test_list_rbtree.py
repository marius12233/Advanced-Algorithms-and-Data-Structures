import unittest
from TdP_collections.map.red_black_tree import RedBlackTreeMap

class TestListRBTree(unittest.TestCase):

    def setUp(self):
        self._T = RedBlackTreeMap()

    def test_catenate(self):
        tree = self._T
        p50 = tree.add(50)
        p30 = tree.add(30)
        p60 = tree.add(60)
        p25 = tree.add(25)
        p35 = tree.add(35)

        tree2 = RedBlackTreeMap()
        p20 = tree2.add(20)

        tree3 = RedBlackTreeMap()
        p10 = tree3.add(10)
        p5 = tree3.add(5)
        p15 = tree3.add(15)

        l = [p50,p20, p60, p10, p30, p5, p15, p25, p35]

        tree.catenate(tree, pivot=tree2.root(), T2=tree3)

        for i, pos in enumerate(tree.breadthfirst()):
            self.assertEqual(pos, l[i])

        tree4 = RedBlackTreeMap()
        p70 = tree4.add(70)

        tree5 = RedBlackTreeMap()
        p80 = tree5.add(80)
        p75 = tree5.add(75)
        p85 = tree5.add(85)

        tree.catenate(tree, pivot=tree4.root(), T2=tree5, left=False)

        l = [p50,p20, p70, p10, p30, p60, p80, p5, p15, p25, p35, p75, p85]

        for i, pos in enumerate(tree.breadthfirst()):
            self.assertEqual(pos, l[i])
            print(pos.key()," = ", l[i].key())


    def test_split(self):
        tree = self._T
        p50 = tree.add(50)
        p20 = tree.add(20)
        p70 = tree.add(70)
        l = tree._l

        T1, T2 = tree.split(p50)

        self.assertEqual(T1.root(), p20)
        self.assertEqual(T2.root(), p70)
        self.assertEqual(len(T1), 1)
        self.assertEqual(len(T2), 1)
        self.assertFalse(T1.root()._node._red)
        self.assertFalse(T2.root()._node._red)
        self.assertEqual(T1.root()._node._black_height, 2)
        self.assertEqual(T2.root()._node._black_height, 2)

        self.assertEqual(l.first(), T1.root()._node._left_out)
        self.assertEqual(l.last(), T2.root()._node._right_out)








