from TdP_collections.map.red_black_tree import RedBlackTreeMap
if __name__=="__main__":
    tree = RedBlackTreeMap()



    p1 = tree.add(43)
    p2 = tree.add(45)
    p3 = tree.add(44)

    l = tree._l
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

    print(root._node._left_out)
    print(root._node._right_out)
    print(left_child._node._left_out is f9)
    
