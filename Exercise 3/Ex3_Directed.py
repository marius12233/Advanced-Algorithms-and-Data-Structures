from graphs.Graph import Graph
from graphs.DFS import *

if __name__ == "__main__":
    """Example number 1 of a directed graph"""
    g1 = Graph(True)

    v0_g1 = g1.insert_vertex(0)
    v1_g1 = g1.insert_vertex(1)
    v2_g1 = g1.insert_vertex(2)
    v3_g1 = g1.insert_vertex(3)
    v4_g1 = g1.insert_vertex(4)

    g1.insert_edge(v1_g1,v0_g1)
    g1.insert_edge(v0_g1,v3_g1)
    g1.insert_edge(v3_g1,v4_g1)
    g1.insert_edge(v4_g1,v0_g1)
    g1.insert_edge(v0_g1,v2_g1)
    g1.insert_edge(v2_g1,v1_g1)

    forest_g1 = DFS(g1,v0_g1)

    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 1 from vertex 0:')
    for e in forest_g1:
        print(forest_g1[e])
    print('')

    """--------------------------------------------------------------------------------------------------------------"""
    """Example number 2 of a directed graph"""
    g2 = Graph(True)

    v0_g2 = g2.insert_vertex(0)
    v1_g2 = g2.insert_vertex(1)
    v2_g2 = g2.insert_vertex(2)
    v3_g2 = g2.insert_vertex(3)

    g2.insert_edge(v0_g2,v1_g2)
    g2.insert_edge(v0_g2,v2_g2)
    g2.insert_edge(v2_g2,v0_g2)
    g2.insert_edge(v1_g2,v2_g2)
    g2.insert_edge(v2_g2,v3_g2)
    g2.insert_edge(v3_g2,v3_g2)

    forest_g2 = DFS(g2,v2_g2)

    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 2 from vertex 2:')
    for e_g2 in forest_g2:
        print(forest_g2[e_g2])
    print('')

    """--------------------------------------------------------------------------------------------------------------"""
    """Example number 3 of a directed graph"""
    g3 = Graph(True)

    v0_g3 = g3.insert_vertex(0)
    v1_g3 = g3.insert_vertex(1)
    v2_g3 = g3.insert_vertex(2)
    v3_g3 = g3.insert_vertex(3)

    g3.insert_edge(v0_g3,v1_g3)
    g3.insert_edge(v1_g3,v2_g3)
    g3.insert_edge(v2_g3,v3_g3)

    forest_g3 = DFS(g3,v0_g3)

    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 3 from vertex 0:')
    for e_g3 in forest_g3:
        print(forest_g3[e_g3])
    print('')

    """--------------------------------------------------------------------------------------------------------------"""
    """Example number 4 of a directed graph"""
    g4 = Graph(True)

    v0_g4 = g4.insert_vertex(0)
    v1_g4 = g4.insert_vertex(1)
    v2_g4 = g4.insert_vertex(2)
    v3_g4 = g4.insert_vertex(3)
    v4_g4 = g4.insert_vertex(4)
    v5_g4 = g4.insert_vertex(5)
    v6_g4 = g4.insert_vertex(6)
    v7_g4 = g4.insert_vertex(7)
    v8_g4 = g4.insert_vertex(8)
    v9_g4 = g4.insert_vertex(9)
    v10_g4 = g4.insert_vertex(10)

    g4.insert_edge(v0_g4,v1_g4)
    g4.insert_edge(v1_g4,v3_g4)
    g4.insert_edge(v3_g4,v7_g4)
    g4.insert_edge(v1_g4,v4_g4)
    g4.insert_edge(v4_g4,v8_g4)
    g4.insert_edge(v4_g4,v9_g4)
    g4.insert_edge(v0_g4,v2_g4)
    g4.insert_edge(v2_g4,v5_g4)
    g4.insert_edge(v5_g4,v10_g4)
    g4.insert_edge(v2_g4,v6_g4)

    forest_g4 = DFS(g4,v0_g4)

    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 4 from vertex 0:')
    for e_g4 in forest_g4:
        print(forest_g4[e_g4])
    print('')

    """--------------------------------------------------------------------------------------------------------------"""
    """Example number 5 of a directed graph"""
    g5 = Graph(True)

    v0_g5 = g5.insert_vertex(0)
    v1_g5 = g5.insert_vertex(1)
    v2_g5 = g5.insert_vertex(2)

    g5.insert_edge(v0_g5,v1_g5)
    g5.insert_edge(v2_g5,v1_g5)

    forest_g5 = DFS(g5,v0_g5)
    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 5 from vertex 0:')
    if len(forest_g5) != 0:
        for e_g5 in forest_g5:
            print(forest_g5[e_g5])
    else:
        print('There is no result')
    print('')

    forest_g5 = DFS(g5,v1_g5)
    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 5 from vertex 1:')
    if len(forest_g5) != 0:
        for e_g5 in forest_g5:
            print(forest_g5[e_g5])
    else:
        print('There is no result')
    print('')

    forest_g5 = DFS(g5,v2_g5)
    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 5 from vertex 2:')
    if len(forest_g5) != 0:
        for e_g5 in forest_g5:
            print(forest_g5[e_g5])
    else:
        print('There is no result')
    print('')

    """--------------------------------------------------------------------------------------------------------------"""
    """Example number 6 of a directed graph"""
    g6 = Graph(True)

    v0_g6 = g6.insert_vertex(0)

    forest_g6 = DFS(g6,v0_g6)

    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 6 from vertex 0:')
    if len(forest_g6) != 0:
        for e_g6 in forest_g6:
            print(forest_g6[e_g6])
    else:
        print('There is no result')
    print('')
