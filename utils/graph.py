class Graph:
    def __init__(self, nodes: set[str] = set(), edges: set[tuple] = []) -> None:
        self.nodes = nodes
        self.edges = edges

    @staticmethod
    def from_edges(edges: set[tuple]):
        nodes = set([item for sublist in edges for item in sublist])

        graph = Graph(
            nodes=nodes,
            edges=edges
        )

        return graph

    def copy(self):
        return Graph(
            nodes=self.nodes.copy(),
            edges=self.edges.copy()
        )

    def get_neighbours(self, node: str) -> set[str]:
        """Gets the neighbours of a node in an undirected graph.
        Warning: This does not take into account circular references."""

        # Get all edges that contain the node
        connected_edges = [edge for edge in self.edges if node in edge]

        # Get all nodes that are connected to the node
        nodes = set([item for sublist in connected_edges for item in sublist])

        # Remove the node itself if present
        if node in nodes:
            nodes.remove(node)

        return nodes

    def remove_node(self, node: str):
        """Removes a node from an undirected graph."""
        self.nodes.remove(node)
        self.edges = set([edge for edge in self.edges if node not in edge])

    def draw_graph(self):
        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.Graph()

        for edge in self.edges:
            G.add_edge(edge[0], edge[1])

        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
