from utils.graph import Graph


def test_graph_from_edges():
    edges = [
        ('a', 'b'),
        ('b', 'c')
    ]

    graph = Graph.from_edges(edges)

    assert graph.nodes == {'a', 'b', 'c'}, "Should be {'a', 'b', 'c'}"
    assert graph.edges == [('a', 'b'), ('b', 'c')], "Should be [('a', 'b'), ('b', 'c')]"


def test_graph_get_neighbours():
    edges = [
        ('a', 'b'),
        ('b', 'c'),
        ('c', 'a')
    ]

    graph = Graph.from_edges(edges)

    neighbours = graph.get_neighbours('a')

    assert neighbours == {'b', 'c'}, "Should be {'b', 'c'}"


def test_remove_node():
    edges = [
        ('a', 'b'),
        ('b', 'c'),
        ('c', 'a'),
        ('d', 'e'),
        ('e', 'f')
    ]

    graph = Graph.from_edges(edges)

    graph.remove_node('a')

    assert graph.nodes == {'b', 'c', 'd', 'e', 'f'}, "Should be {'b', 'c', 'd', 'e', 'f'}"
    assert graph.edges == {('d', 'e'), ('e', 'f'), ('b', 'c')}, "Should be {('d', 'e'), ('e', 'f'), ('b', 'c')}"

    graph.remove_node('f')

    assert graph.nodes == {'b', 'c', 'd', 'e'}, "Should be {'b', 'c', 'd', 'e'}"
    assert graph.edges == {('d', 'e'), ('b', 'c')}, "Should be {('d', 'e'), ('b', 'c')}"

    graph.remove_node('d')
    graph.remove_node('e')
    graph.remove_node('b')

    assert graph.nodes == {'c'}, "Should be {'c'}"
    assert graph.edges == set(), "Should be set()"

    graph.remove_node('c')

    assert graph.nodes == set(), "Should be set()"
    assert graph.edges == set(), "Should be set()"
