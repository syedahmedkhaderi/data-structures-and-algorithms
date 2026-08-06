# Graph Data Structures & Algorithms in Python

A collection of Python implementations and Jupyter Notebooks covering fundamental graph data structures, traversal techniques, shortest path algorithms, and minimum spanning trees.

## Features & Topics Covered

- **Basic Implementations**: Graph creation using adjacency lists (`01-graph-implementation.ipynb`).
- **Traversals**: Breadth-First Search (BFS) and Depth-First Search (DFS) (`02-bfs-and-dfs.ipynb`).
- **Topological Sort**: Directed Acyclic Graph (DAG) ordering (`03-topological-sort.ipynb`).
- **Disjoint Set (Union-Find)**: Optimizations with rank and path compression (`04-disjoint-sets.ipynb`, `DisjointSet.py`).
- **Single Source Shortest Path (SSSP)**:
  - BFS (unweighted graphs)
  - Dijkstra's Algorithm (weighted graphs without negative edges)
  - Bellman-Ford Algorithm (handles negative weight edges & detects negative cycles)
  - Includes comparative analysis across SSSP algorithms.
- **All-Pairs Shortest Path (APSP)**:
  - Floyd-Warshall Algorithm.
- **Minimum Spanning Tree (MST - Greedy)**:
  - Kruskal's Algorithm (with Disjoint Set)
  - Prim's Algorithm.

## Directory Structure

```
12-Graphs/
├── 01-graph-implementation.ipynb
├── 02-bfs-and-dfs.ipynb
├── 03-topological-sort.ipynb
├── 04-disjoint-sets.ipynb
├── SSSP/
│   ├── 01-bfs-SSSP.ipynb
│   ├── 02-DijkstraSSSP.ipynb
│   └── 03-BellmanFord.ipynb
├── APSP/
│   └── 01-Floyd-Warshall.ipynb
└── MST - Greedy/
    ├── 01-Kruskal.ipynb
    ├── 02-Prim's.ipynb
    └── DisjointSet.py
```


