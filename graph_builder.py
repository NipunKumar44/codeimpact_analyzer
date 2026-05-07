import networkx as nx

def build_graph(parsed_data):

    graph = nx.DiGraph()

    for func in parsed_data:

        graph.add_node(func["name"])

        for called in func["calls"]:

            graph.add_edge(func["name"], called)

    return graph