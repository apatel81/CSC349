
def SmartGreedyVC(G):
    c = []
    # print(G.graph)
    while G.is_empty() == False:
        max = 0
        for i in G.graph:
            if len(G.graph[i]) > max:
                max = len(G.graph[i])
                vertex = i

        # print(vertex, max)

        for i in G.graph:
            if vertex in G.graph[i]:
                G.graph[i].remove(vertex)

        del G.graph[vertex]
        # print(G.graph)
        c.append(vertex)
    return c


def approximation(G):
    c = []

    while G.is_empty() == False:
        u = next(iter(G.graph))
        v = (next(iter(G.graph.values())))
        v = v[0]

        # print(G.graph)
        # print(u, v)
        # print("This is my test:", G.graph[u][0])

        for i in G.graph:
            if u in G.graph[i]:
                G.graph[i].remove(u)
            if v in G.graph[i]:
                G.graph[i].remove(v)

        del G.graph[u]
        del G.graph[v]
        # print(G.graph)

        c.append(u)
        c.append(v)
    return c


def brute(G):
    c = []
    visited = [False] * G.num_vertices

    for i in G.graph:
        if visited[i] == False:
            c.append(i)
            visited[i] = True
            for j in G.graph:
                if visited[j] == False:
                    visited[j] = True
                    break

    # true = []
    # for i in visited:
    #     if visited[i] == True:
    #         true.append(i)
    # print(c)
    return c



