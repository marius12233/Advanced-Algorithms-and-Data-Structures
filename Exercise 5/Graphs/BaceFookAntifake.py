def BaceFook_antifake(g):
    # Initialization of the list that will be used and returned after the end of the execution of the algorithm
    # This list contains all the computers where the software will be installed
    installed_vertices = []

    # Beginning of the execution of the algorithm
    for u in g.vertices():
        #the examined vertex 'u' must be not installed and it must have no installed adjacent vertices otherwise the loop restarts
        if not u.get_installed() and g.get_not_installed_adj(u)!=0:
            #the nested loop is applied on the adjacent vertices
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if not v.get_installed():
                    #if the number of adjacent vertices of v, which do not have the software is bigger or equal than the
                    #number of the vertex 'u', the software is installed on 'v', otherwise it is installed on 'u'
                    if g.get_not_installed_adj(v) >= g.get_not_installed_adj(u):
                        v.set_installed(True)                                 #software installation on 'v'
                        installed_vertices.append(v)                          #update of the installed vertices' list
                        g.decrease_not_installed_adj(u,True)                  #decreasing of 'u' not installed adjacent vertices
                    else:
                        u.set_installed(True)                                 #software installation on 'u'
                        installed_vertices.append(u)                          #update of the installed vertices' list
                        g.decrease_not_installed_adj(u)                       #decreasing of 'u' not installed adjacent vertices
                        break

    return installed_vertices


