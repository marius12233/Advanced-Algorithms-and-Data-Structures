import random
from Graphs.Graph import Graph
from Graphs.BaceFookAntifake import BaceFook_antifake

if __name__ == "__main__":

   installed_vertices=[]

   #Generation of 100 different graphs of 100 nodes
   for i in range(100): #100
        installed_vertices.clear()
        graph = Graph()
        for j in range(100): #100
            graph.insert_vertex(j)

        for u in graph.vertices():
            for v in graph.vertices():
                if v!=u and graph.get_edge(u, v) is None:
                    #the getrandbits() function is used to decide whether to add or not a given edge
                    if random.getrandbits(1):
                        graph.insert_edge(u, v)


        #algorithm execution
        installed_vertices=BaceFook_antifake(graph)

        #PERFORMANCE EVALUATION FOR THE CURRENT GRAPH
        print("GRAPH {}:".format(i))
        print("The number of the installed vertices is: {}".format(len(installed_vertices)))
        print("Installed vertices are:")
        for v in installed_vertices:
            print("{}".format(v))

