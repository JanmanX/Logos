interference = get_interference_graph(program.instructions, kill, live_out)

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edges_from(interference)

nx.draw(G, with_labels=True)
plt.show()
