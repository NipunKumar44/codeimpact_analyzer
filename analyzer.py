import networkx as nx

def find_impacted(graph, target):

    impacted = []

    for node in graph.nodes():

        if node != target:

            if nx.has_path(graph, node, target):

                impacted.append(node)

    return impacted