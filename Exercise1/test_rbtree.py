from TdP_collections.map.red_black_tree import RedBlackTreeMap
if __name__=="__main__":
    #l=PositionalList()
    tree = RedBlackTreeMap()


    l = tree._l
    p1 = tree.add(43)
    p2 = tree.add(45)
    p3 = tree.add(44)

    #l = tree._l
    f7 = l.first()
    f10 = l.after(f7)
    f8 = l.after(f10)
    f9 = l.after(f8)

    root = tree.root()
    left_child = tree.left(root)
    right_child = tree.right(root)

    print(root.key())
    print(left_child.key())
    print(right_child.key())

    print(root._node._left_out is None)
    print(root._node._right_out is None)
    print(left_child._node._left_out == f7)
    print(left_child._node._right_out == f10)
    print(right_child._node._left_out == f8)
    print(right_child._node._right_out == f9)
    print("Len lista: ",len(l))
    print("================= DELETE ==================")


    tree.delete(right_child)
    print(left_child._node._left_out == f7)
    print(left_child._node._right_out == f10)
    print(root._node._right_out==f9)
    print(root._node._left_out is None)
    print("Len lista: ", len(l))
    print(f7._node._parent==left_child)
    print(f10._node._parent==left_child)
    print(f9._node._parent==root)

    print(f7._node._parent.key())
    print(f10._node._parent.key())
    print(f9._node._parent.key())

