from Exercise1.b_tree import BTree

if __name__=="__main__":
    btree = BTree()
    btree.add(10)
    btree.add(15)
    btree.add(5)
    btree.add(20)
    btree.add(30)
    btree.add(40)


    print(btree._num_node)
    #btree.add(60)

    print("BREADTHFIRST OF RADIX (NO SPLITTING)")
    for child in btree.BFS():
       print(child)

    print("\nAdding 25 \n")
    btree.add(25)
    print("BREADTHFIRST AFTER SPLITTING")
    for child in btree.BFS():
       print(child)
    #print(btree.root()._tree)

    btree.add(80)
    btree.add(85)
    btree.add(90)
    btree.add(95)
    btree.add(100)
    btree.add(101)
    btree.add(102)
    #btree.add(89)
    btree.add(92)
    #btree.add(93)
    #btree.delete(25)
    #btree.delete(101)
    for i in range(110,120):
        btree.add(i)
    #btree.delete(112)
    btree.delete(20)
    btree.delete(80)
    btree.delete(10)
    btree.delete(95)
    btree.delete(112)



    for child in btree.BFS():
       print(child, "   BH: ", child._node._black_height, " is red: ", child._node._red, " size: ", child._container._size,
             " list_size: ", child._container._l._size)

    print((btree.search(btree.root(), 10)[0]).key())



