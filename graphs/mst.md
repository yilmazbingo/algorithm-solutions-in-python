- Spanning tree, if you cover all edges with minimum number of edges
- it is a subset of graph. Because number of edges alway less than or equal to the number of edges in graph
- spanning tree cannot be disconnected. graph should be single component in order to find the spanning tree.
- spanning tee has V-1 edges. we can never have any cycle in spanning tree because we are covering V vertices with V-1 edges
- IMPORTANT! ALL the spannig trees have same number of edges
- a connected undirected graph has at least one spanning tree
- A complete undirected graph (fully-connected-graph) has N over N-2 number of different spanning trees. N is number of vertices
  **Fully Connected Graph** It is a connected graph where a unique edge connected each pair of vertices. In other words, for every two vertices, there is a distinct edge.
- spanning tree is minimally connected. removing one edge will disconnect the graph

### Minimum spanning tree
A spanning tree with min cost in a weighted graph. There could be more than one MST.

- Design Network Cable route for cities using minimum cable, hence minimizing cost. 
- Design water supply in network design
- select min value option first
## STEPS
- we can start from any single node. we are gonna perform bfs on that node. 
- we are gonna have `visit` set not to have a cycle. 
- min-heap is gonna keep track of our frontier. frontier, is every possible node that could be added from this position. 
-  we add (cost,frontier) to min_heap. when we pop, we want to see the next node with the minimum possible cost