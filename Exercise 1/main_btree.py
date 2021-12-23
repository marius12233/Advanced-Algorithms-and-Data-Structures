from b_tree import BTree

if __name__=="__main__":
    btree = BTree()

    btree.add(10)
    btree.add(15)
    btree.add(5, ('Mario', 20, 'Bellizzi'))
    btree.add(20)
    btree.add(30)
    btree.add(40)

    print("BREADTHFIRST BEFORE SPLITTING")

    btree.print_tree()

    btree.add(25)
    print("BREADTHFIRST AFTER SPLITTING")

    btree.print_tree()

    btree.add(80)
    btree.add(85)
    btree.add(90)
    btree.add(95)
    btree.add(100)
    btree.add(101)
    btree.add(102)
    btree.add(92)

    for i in range(110,120):
        btree.add(i)

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

    btree.delete(10)

    print(" IT WILL DELETE 85")
    print("\nBREADTHFIRST BEFORE TRANSFER: \n")
    btree.print_tree()
    btree.delete(85)
    print("\nBREADTHFIRST AFTER TRANSFER: ")
    btree.print_tree()

    btree.delete(119)

    print(" IT WILL DELETE 118")
    print("\nBREADTHFIRST BEFORE FUSION: \n")
    btree.delete(118)
    print("\nBREADTHFIRST AFTER FUSION: ")
    btree.print_tree()
    print("Searching for element 5")
    print(btree.search_key(5))




