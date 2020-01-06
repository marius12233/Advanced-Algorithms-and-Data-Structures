from AADS.TdP_collections.map.red_black_tree import RedBlackTreeMap

if __name__=="__main__":
    #l=PositionalList()
    tree = RedBlackTreeMap()
    #
    #
    l = tree._l
    p1 = tree.add(45)
    print("ELEMENTI NODO:")
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())

    p2=tree.add(48)
    print("ELEMENTI NODO:")
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())
    p3=tree.add(44)
    print("ELEMENTI NODO:")
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())
    p10 = tree.add(49)
    print("ELEMENTI NODO:")
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())
    p9 = tree.add(46)
    print("ELEMENTI NODO:")
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())
    p4=tree.add(50)
    print("ELEMENTI NODO:")
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())

    p11=tree.add(47)
    print("ELEMENTI NODO:")
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())
    p5=tree.add(60)
    print("ELEMENTI NODO:")
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())
    p6=tree.add(43)
    print("ELEMENTI NODO:")
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())
    p7=tree.add(40)
    print("ELEMENTI NODO:")
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())
    p8=tree.add(70)
    print("ELEMENTI NODO:")
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())


    tree.delete(p11)
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())

    tree.delete(p4)
    for element in l:
        print(element._node._parent.key())
        print(element._node)

    print("MEDIANO:")
    print(l._median)
    print(l._median._parent.key())


