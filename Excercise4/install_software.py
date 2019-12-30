from TdP_collections.graphs.dfs import *

def min_nodes_install(tree):

    forest = DFS_complete(tree)
    l = []
    for vertex in forest.keys():
        l.append(vertex)

    reversed_l = l[::-1]

    dp = {}
    mark = {}

    for v in reversed_l:
        if tree.is_leaf(v):
            dp[v] = [1, 0]
            mark[v] = "S/N"
        else:
            dp[v] = [None, None]
            # dp[v][True] = dp[v][1] means I took parent of v so, I can choose to don't take v
            # dp[v][False] = dp[v][0] means I don't took parent of v, so I have to take v
            # Don't take parent of v, so I have to take v -> call all dp of the children of v with state True because the parent v is taken
            taken_value = 1 + sum([dp[child][1] for child in tree.children(v)])  # I take it
            not_taken_value = sum([dp[child][0] for child in tree.children(v)])  # I don't take it
            dp[v][0] = taken_value
            dp[v][1] = min(taken_value,not_taken_value)
            if taken_value == not_taken_value:
                mark[v] = "S/N"
            if taken_value < not_taken_value:
                mark[v] = "S"
            else:
                mark[v] = "N"

    return find_solution(tree, dp, mark, l)


def find_solution(tree, dp, mark, l):

    installed = {}

    for v in l:
        parent = tree.parent(v)

        if parent is not None and installed[parent]==False:
            installed[v] = True
        else:
            if mark[v] == "S":
                installed[v]=True
            if mark[v] == "N":
                installed[v]=False
            if mark[v] == "S/N":
                installed[v] = False

                if tree.is_root(v):
                    for child in tree.children(v):
                        if mark[child]=="N": # Se c'è un solo figlio che non deve essere preso
                            installed[v]=True
                            break

        print(v, "  ", dp[v], "  ", mark[v], " installed: ", installed[v])
    return installed
