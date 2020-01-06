from general_tree import *
from install_software import *

if __name__ == "__main__":
    """Example number 1 of a general tree"""
    tree1 = GeneralTree()
    root1 = tree1.add_root(1)
    a1 = tree1.add_child(root1, 2)
    b1 = tree1.add_child(root1, 3)
    c1 = tree1.add_child(root1, 4)
    d1 = tree1.add_child(a1, 5)
    e1 = tree1.add_child(a1, 6)
    f1 = tree1.add_child(b1, 7)
    g1 = tree1.add_child(b1, 8)

    print('Results for the example number 1')
    solution1 = min_nodes_install(tree1)
    print(' ')

    """--------------------------------------------------------------------------------------------------------------"""
    """Example number 2 of a general tree"""
    tree2 = GeneralTree()
    root2 = tree2.add_root(1)
    a2 = tree2.add_child(root2, 2)
    b2 = tree2.add_child(root2, 3)
    c2 = tree2.add_child(root2, 4)
    d2 = tree2.add_child(root2, 5)
    e2 = tree2.add_child(a2, 6)
    f2 = tree2.add_child(b2, 7)
    g2 = tree2.add_child(b2, 8)
    h2 = tree2.add_child(b2, 9)
    i2 = tree2.add_child(c2, 10)
    j2 = tree2.add_child(c2, 11)
    k2 = tree2.add_child(g2, 12)

    print('Results for the example number 2')
    solution2 = min_nodes_install(tree2)
    print(' ')

    """--------------------------------------------------------------------------------------------------------------"""
    """Example number 3 of a general tree"""
    tree3 = GeneralTree()
    root3 = tree3.add_root(1)
    a3 = tree3.add_child(root3, 2)
    b3 = tree3.add_child(root3, 3)
    c3 = tree3.add_child(root3, 4)
    d3 = tree3.add_child(root3, 5)
    e3 = tree3.add_child(a3, 6)
    f3 = tree3.add_child(a3, 7)
    g3 = tree3.add_child(a3, 8)
    h3 = tree3.add_child(a3, 9)
    i3 = tree3.add_child(e3, 10)
    j3 = tree3.add_child(g3, 11)
    k3 = tree3.add_child(g3, 12)
    l3 = tree3.add_child(h3, 13)
    m3 = tree3.add_child(l3, 14)
    n3 = tree3.add_child(l3, 15)
    o3 = tree3.add_child(b3, 16)
    p3 = tree3.add_child(o3, 17)
    q3 = tree3.add_child(d3, 18)
    r3 = tree3.add_child(d3, 19)
    s3 = tree3.add_child(q3, 20)
    t3 = tree3.add_child(s3, 21)
    u3 = tree3.add_child(s3, 22)

    print('Results for the example number 3')
    solution3 = min_nodes_install(tree3)
    print(' ')

    """--------------------------------------------------------------------------------------------------------------"""
    """Example number 4 of a general tree"""
    tree4 = GeneralTree()
    root4 = tree4.add_root(1)
    a4 = tree4.add_child(root4, 2)
    b4 = tree4.add_child(a4, 3)
    c4 = tree4.add_child(a4, 4)
    d4 = tree4.add_child(a4, 5)
    e4 = tree4.add_child(d4, 6)
    f4 = tree4.add_child(d4, 7)
    g4 = tree4.add_child(e4, 8)
    h4 = tree4.add_child(e4, 9)
    i4 = tree4.add_child(e4, 10)
    j4 = tree4.add_child(e4, 11)

    print('Results for the example number 4')
    solution4 = min_nodes_install(tree4)
    print(' ')
