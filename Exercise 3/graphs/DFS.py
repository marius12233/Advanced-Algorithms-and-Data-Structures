def DFS(g, vertex):
    """ Perform iterative DFS without auxiliary data structures for the entire graph and return forest as a dictionary.
    Newly discovered vertices will be added to the dictionary as a result.
    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.) """

    # Initialization of the forest that will be used and returned after the end of the execution of the DFS algorithm.
    forest = {}

    # Initialization of the graph vertices before the execution of the DFS algorithm (we've considered the case in which
    # this algorithm can be called more than once).
    for u in g.vertices():
        u.set_visited(False)
        u.set_discoverer(None)
        u.set_adj_vertices(g.degree(u))

    # Beginning of the execution of the iterative DFS algorithm without the use of auxiliary data structures
    vertex.set_visited(True)
    stop = False
    while not stop:
        # Checking if the vertex has incident edges (in particular, if the graph is directed, there could be one or
        # more vertices without outgoing edges)
        if vertex.get_adj_vertices() != 0:
            for e in g.incident_edges(vertex):                                   # for every (outgoing) edge from vertex
              v = e.opposite(vertex)
              if not v.get_visited():                                            # checking if v is an unvisited vertex
                  v.set_visited(True)                                            # assigning true to the unvisited vertex v
                  forest[v] = e                                                  # e is the tree edge that discovered v
                  vertex.set_adj_vertices(g.degree(vertex))                      # resetting the number of adjacent vertices
                  v.set_discoverer(vertex)                                       # storing the discoverer vertex of v
                  vertex = v
                  break
              else:
                  vertex.set_adj_vertices(vertex.get_adj_vertices() - 1)
                  if vertex.get_adj_vertices() == 0:
                      if vertex.get_discoverer() is not None:
                          vertex = vertex.get_discoverer()

                          while vertex.get_adj_vertices() == 0:                  # The while cycle is used to go back to the
                                vertex = vertex.discoverer                       # vertex that still has unexplored edges.

                      else:
                          stop = True
        else:
            # If the vertex has no incident edges (in the case of a directed graph, the vertex has no outgoing edges),
            # then the vertex becomes its discoverer, if this value isn't None
            if vertex.get_discoverer() is not None:
                vertex = vertex.get_discoverer()
            else:
                # If the graph is composed only by one single vertex (a very extreme case) or more vertices that aren't
                # connected and are the one where the DFS algorithm has been called, then the cycle is stopped
                stop = True

    return forest