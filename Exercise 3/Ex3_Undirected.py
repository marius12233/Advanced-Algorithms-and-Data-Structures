from graphs.Graph import Graph
from graphs.DFS import *

if __name__ == "__main__":
    """Example number 1 of an undirected graph"""
    g1 = Graph()

    v0_g1 = g1.insert_vertex(0) #A
    v1_g1 = g1.insert_vertex(1) #B
    v2_g1 = g1.insert_vertex(2) #C
    v3_g1 = g1.insert_vertex(3) #D
    v4_g1 = g1.insert_vertex(4) #E

    g1.insert_edge(v1_g1,v0_g1)
    g1.insert_edge(v0_g1,v3_g1)
    g1.insert_edge(v4_g1,v0_g1)
    g1.insert_edge(v0_g1,v2_g1)
    g1.insert_edge(v1_g1,v2_g1)
    g1.insert_edge(v2_g1,v3_g1)
    g1.insert_edge(v2_g1,v4_g1)

    forest_g1 = DFS(g1,v0_g1)

    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 1 from vertex 0')
    for e_g1 in forest_g1:
        print(forest_g1[e_g1])
    print('')

    """--------------------------------------------------------------------------------------------------------------"""
    """Example number 2 of an undirected graph"""
    g2 = Graph()

    v0_g2 = g2.insert_vertex(0) #A
    v1_g2 = g2.insert_vertex(1) #B
    v2_g2 = g2.insert_vertex(2) #C
    v3_g2 = g2.insert_vertex(3) #D
    v4_g2 = g2.insert_vertex(4) #E

    g2.insert_edge(v0_g2,v1_g2)
    g2.insert_edge(v0_g2,v2_g2)
    g2.insert_edge(v0_g2,v3_g2)
    g2.insert_edge(v2_g2,v1_g2)
    g2.insert_edge(v2_g2,v4_g2)

    forest_g2 = DFS(g2,v0_g2)

    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 2 from vertex 0')
    for e_g2 in forest_g2:
        print(forest_g2[e_g2])
    print('')

    """--------------------------------------------------------------------------------------------------------------"""
    """Example number 3 of an undirected graph"""
    g3 = Graph()

    v0_g3 = g3.insert_vertex(0) #A
    v1_g3 = g3.insert_vertex(1) #B
    v2_g3 = g3.insert_vertex(2) #C
    v3_g3 = g3.insert_vertex(3) #D
    v4_g3 = g3.insert_vertex(4) #E
    v5_g3 = g3.insert_vertex(5) #F
    v6_g3 = g3.insert_vertex(6) #G

    g3.insert_edge(v0_g3,v1_g3)
    g3.insert_edge(v1_g3,v3_g3)
    g3.insert_edge(v1_g3,v5_g3)
    g3.insert_edge(v5_g3,v4_g3)
    g3.insert_edge(v0_g3,v2_g3)
    g3.insert_edge(v2_g3,v6_g3)
    g3.insert_edge(v0_g3,v4_g3)

    forest_g3 = DFS(g3,v0_g3)

    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 3 from vertex 0')
    for e_g3 in forest_g3:
        print(forest_g3[e_g3])
    print('')

    """--------------------------------------------------------------------------------------------------------------"""
    """Example number 4 of an undirected graph"""
    g4 = Graph()

    v0_g4 = g4.insert_vertex(0)
    v1_g4 = g4.insert_vertex(1)
    v2_g4 = g4.insert_vertex(2)
    v3_g4 = g4.insert_vertex(3)
    v4_g4 = g4.insert_vertex(4)
    v5_g4 = g4.insert_vertex(5)

    g4.insert_edge(v0_g4,v1_g4)
    g4.insert_edge(v1_g4,v3_g4)
    g4.insert_edge(v1_g4,v4_g4)
    g4.insert_edge(v3_g4,v4_g4)
    g4.insert_edge(v3_g4,v5_g4)
    g4.insert_edge(v4_g4,v5_g4)
    g4.insert_edge(v0_g4,v2_g4)
    g4.insert_edge(v2_g4,v4_g4)

    forest_g4 = DFS(g4,v0_g4)

    # Results of the execution of the iterative DFS without auxiliary data structures
    print('Results of graph number 4 from vertex 0')
    for e_g4 in forest_g4:
        print(forest_g4[e_g4])
    print('')
