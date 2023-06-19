from IL.RegisterAllocator import *

def test_colors():
    graph = Graph.from_edges([
        ('a', 'b'),
        ('b', 'c'),
        ('c', 'a'),
        ('d', 'e'),
        ('e', 'f'),
        ('a', 'd')
    ])

    print(color_graph(graph, 3))

