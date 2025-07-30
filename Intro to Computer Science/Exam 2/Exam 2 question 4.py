def reverseGraph(g):
    newGraph = {}
    for node in g:
        #print(node)
        newGraph[node] = []

    for node in g:
        for edge in g[node]:
            newGraph[edge].append(node)

    return newGraph
