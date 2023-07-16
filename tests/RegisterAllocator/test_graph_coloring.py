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
    colors = color_graph(graph, 3)

    test = colors


def test_spill():
    graph = Graph.from_edges([
        ('a', 'b'),
        ('b', 'c'),
        ('c', 'a')
        ])
    colors = color_graph(graph, 2)

    # Assert one of the colors is spilled ("spill")
    assert 'spill' in colors.values()



def test_colors2():
    # Test coloring with 5 registers with a circular graph
    graph = Graph.from_edges([
        ('a', 'b'),
        ('b', 'c'),
        ('c', 'd'),
        ('d', 'e'),
        ('e', 'a')
    ])

    colors = color_graph(graph, 3)

    assert 'spill' not in colors.values()

