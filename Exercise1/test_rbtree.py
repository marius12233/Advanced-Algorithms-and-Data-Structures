from TdP_collections.map.red_black_tree import RedBlackTreeMap
if __name__=="__main__":
    #l=PositionalList()
    tree = RedBlackTreeMap()
    #
    #
    # l = tree._l
    # p1 = tree.add(43)
    # p2 = tree.add(45)
    # p3 = tree.add(44)
    #
    # #l = tree._l
    # f7 = l.first()
    # f10 = l.after(f7)
    # f8 = l.after(f10)
    # f9 = l.after(f8)
    #
    # root = tree.root()
    # left_child = tree.left(root)
    # right_child = tree.right(root)
    #
    # print(root.key())
    # print(left_child.key())
    # print(right_child.key())
    #
    # print(root._node._left_out is None)
    # print(root._node._right_out is None)
    # print(left_child._node._left_out == f7)
    # print(left_child._node._right_out == f10)
    # print(right_child._node._left_out == f8)
    # print(right_child._node._right_out == f9)
    # print("Len lista: ",len(l))
    # print("================= DELETE ==================")
    #
    #
    # tree.delete(right_child)
    # print(left_child._node._left_out == f7)
    # print(left_child._node._right_out == f10)
    # print(root._node._right_out==f9)
    # print(root._node._left_out is None)
    # print("Len lista: ", len(l))
    # print(f7._node._parent==left_child)
    # print(f10._node._parent==left_child)
    # print(f9._node._parent==root)
    #
    # print(f7._node._parent.key())
    # print(f10._node._parent.key())
    # print(f9._node._parent.key())
    #
    #

    print("="*20+" ELEMENTI ALBERO "+"="*20)
    p1 = tree.add(50)
    p2 = tree.add(30)
    p3 = tree.add(60)
    p4 = tree.add(25)
    p5 = tree.add(35)
    #p6 = tree.add(27)
    #p7 = tree.add(28)
    #p8 = tree.add(29)
    print("Before delete")
    print(p1.key(), " ", p1._node._black_height)
    print(p2.key(), " ", p2._node._black_height)
    print(p3.key(), " ", p3._node._black_height)
    print(p4.key(), " ", p4._node._black_height)
    print(p5.key(), " ", p5._node._black_height)
    #print(p6.key(), " ", p6._node._black_height)
    #print(p7.key(), " ", p7._node._black_height)
    #print(p8.key(), " ", p8._node._black_height)

    p = tree._find_black_height(tree, 2)
    print("Found node: ",p.key(), " with black height: ", p._node._black_height, " with color: ", p._node._red)

    tree2 = RedBlackTreeMap()
    tree2.add(20)

    tree3 = RedBlackTreeMap()
    tree3.add(10)
    tree3.add(5)
    tree3.add(15)

    tree.catenate(tree, pivot=tree2.root(), T2=tree3)

    for pos in tree.breadthfirst():
        print(pos.key(), "  black height: ", pos._node._black_height,
              "   red: ", pos._node._red, "    left_out: ", pos._node._left_out, "    right_out: ", pos._node._right_out)






    # tree.delete(p8)
    # tree.delete(p3)
    # tree.delete(p4)
    # tree.delete(p5)
    # tree.delete(p7)
    # tree.delete(p1)
    # tree.delete(p6)
    # print("After delete")
    #print(p1.key(), " ", p1._node._black_height)
    #print(p2.key(), " ", p2._node._black_height)
    #print(p3.key(), " ", p3._node._black_height)
    #print(p4.key(), " ", p4._node._black_height)
    #print(p5.key(), " ", p5._node._black_height)
    #print(p6.key(), " ", p6._node._black_height)
    #print(p7.key(), " ", p7._node._black_height)


    # l = tree._l
    # f1 = l.first()
    # print(f1 == p4._node._left_out)
    # print(f1._node._parent == p4)
    # f2 = l.after(f1)
    # print(f2 == p4._node._right_out)
    # print(f2._node._parent == p4)
    # f3 = l.after(f2)
    # print(f3 == p7._node._left_out)
    # print(f3._node._parent == p7)
    # f4 = l.after(f3)
    # print(f4 == p8._node._left_out)
    # print(f4._node._parent == p8)
    # f5 = l.after(f4)
    # print(f5 == p8._node._right_out)
    # print(f5._node._parent == p8)
    # f6 = l.after(f5)
    # f7 = l.after(f6)
    # print(f6 == p5._node._left_out)
    # print(f6._node._parent == p5)
    # print(f7 == p5._node._right_out)
    # print(f7._node._parent == p5)
    # f8 = l.after(f7)
    # f9 = l.after(f8)
    # print(f8 == p3._node._left_out)
    # print(f8._node._parent == p3)
    # print(f9 == p3._node._right_out)
    # print(f9._node._parent == p3)
    #
    # print(p1._node._left_out == p1._node._right_out == None)
    # print(p2._node._left_out == p2._node._right_out == None)
    # print(p6._node._left_out == p6._node._right_out == None)
    #
    # print(p7._node._right_out == None)



    #p7 = tree.add(65)


    # for pos in tree.breadthfirst():
    #     print(pos.key())
    #
    # print("="*20+" ELEMENTI ALBERO DOPO SPLIT "+"="*20)
    #
    # T1, T2 = tree.split(p5)
    #
    #
    #
    # print("=" * 20 + " ELEMENTI T1 " + "=" * 20)
    #
    # #print(T1.root().key())
    #
    # print("size T1: ", len(T1))
    #
    # for pos in T1.breadthfirst():
    #     print(pos.key())
    #
    # print("=" * 20 + " ELEMENTI T2 " + "=" * 20)
    #
    # #print(T2.root().key())
    # print("size T2: ", len(T2))
    # for pos in T2.breadthfirst():
    #     print(pos.key())



