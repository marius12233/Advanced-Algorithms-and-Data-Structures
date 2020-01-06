from Exercise1.b_tree import BTree
if __name__=="__main__":
    print("="*20," BTREE ", "="*20)
    btree = BTree()
    inp = input("What do you want to do?\n 1) add\n 2) delete\n 3) search\n 4) print\n 5) exit\n")
    inp = int(inp)
    while not inp == 5:
        if inp == 1:
            k = input("Insert key to add: ")
            v = input("Insert value for key k: ")
            btree.add(k,v)
        elif inp == 2:
            k = int(input("Insert key to delete: "))
            btree.delete(k)
        elif inp == 3:
            k = int(input("Insert key to search: "))
            btree.search_key(k)
        elif inp == 4:
            btree.print_tree()

        inp = int(input("What do you want to do?\n 1) add\n 2) delete\n 3) search\n 4) print\n 5) exit\n"))


