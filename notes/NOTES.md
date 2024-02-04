# Notes

## Coding
### Liveness Analysis
```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from(graph.edges)

plt.clf()
nx.draw(G, with_labels=True)
plt.show()
```

## Building
To generate parsers:
```bash
$ antlr4 -Dlanguage=Python3 -visitor -o ./generated Logos.g4
```

## Assembling
```bash
$ as -o program.o program.as
```

## Linking
```bash
$ ld -o program program.o
```


## Debugging
### LLDB

Setting breakpoint
```
(lldb) breakpoint set --name main
```

Reading registers:
```
(lldb) register read
```
