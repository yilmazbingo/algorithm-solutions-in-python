E for edges, V total vertices

- In a complete graph, every pair of vertices is connected by an edge. So the number of edges is just the number of pairs of vertices. 
 That's  n combination 2, which is equal to n(n−1)/2.
  it is asking "How many different combinations do you get if you have n items and choose 2"

- min_heap always keep the shortest path on top. it takes O(logN)

## What is the maximum size of heap can get?

Some nodes can be added twice. so maximum V^2. getting the minimum value will be 

    Log(V^2) = 2 Log(V)

I am going to do this operation for each edge. 

    2 * E * Log(V)

Since E=  V(V−1)/2

     V(V−1) * Log(V)

 E=V^2. edges can be bidirectinal. max_size of heap could be V^2. Some of the nodes could be addes to the heap multiple times. 