
import graph
import subgraph_isomorphism as si

# graph_g = graph.read_graph(sys.argv[1])
# k = int(sys.argv[2])

def k_clique(graph_g, k):
    graph_h = graph.Graph(k)
    # print(graph_h.matrix)

    for i in range(k):
        for j in range(k):
            if i != j:
                graph.add_edge(graph_h, i, j)

    # print(graph_h.matrix)

    subgraph = si.isomorphic_subgraph(graph_g, graph_h)
    # print(subgraph)
    return subgraph
