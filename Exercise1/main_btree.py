from Exercise1.b_tree import BTree

if __name__=="__main__":
    btree = BTree()

    btree.add(10)
    btree.add(15)
    btree.add(5, ('Mario', 20, 'Bellizzi'))
    btree.add(20)
    btree.add(30)
    btree.add(40)


    #print(btree._num_node)
    #btree.add(60)

    print("BREADTHFIRST BEFORE SPLITTING")
    # for child in btree.BFS():
    #    print(child)
    btree.print_tree()

    #print("\nAdding 25 \n")
    btree.add(25)
    print("BREADTHFIRST AFTER SPLITTING")
    # for child in btree.BFS():
    #    print(child)
    #print(btree.root()._tree)
    btree.print_tree()

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
    #btree.add(16)
    #btree.delete(112)
    print(" IT WILL DELETE 20")
    print("\nBREADTHFIRST BEFORE FUSION: \n")
    btree.print_tree()
    btree.delete(20)
    print("\nBREADTHFIRST AFTER FUSION: ")
    btree.print_tree()

    print(" IT WILL DELETE 111")
    print("\nBREADTHFIRST BEFORE TRANSFER: \n")
    btree.print_tree()
    btree.delete(111)
    print("\nBREADTHFIRST AFTER TRANSFER: ")
    btree.print_tree()


    btree.delete(80)


    # print(" IT WILL DELETE 10")
    # print("\nBREADTHFIRST BEFORE TRANSFER: \n")
    # btree.print_tree()
    btree.delete(10)
    #print("\nBREADTHFIRST AFTER TRANSFER: ")
    #btree.print_tree()
    #btree.delete(40)
    #btree.delete(85)
    print(" IT WILL DELETE 85")
    print("\nBREADTHFIRST BEFORE TRANSFER: \n")
    btree.print_tree()
    btree.delete(85)
    print("\nBREADTHFIRST AFTER TRANSFER: ")
    btree.print_tree()

    btree.delete(119)

    print(" IT WILL DELETE 118")
    print("\nBREADTHFIRST BEFORE FUSION: \n")
    #btree.print_tree()
    btree.delete(118)
    print("\nBREADTHFIRST AFTER FUSION: ")
    btree.print_tree()
    print("Searching for element 5")
    print(btree.search_key(5))




