## BELLMAN-FORD
0(E * K) edges and K parameter given. In general Bellman-Ford runs in O(E*V)
stop point is the number of points between start-destination
- Bellman-ford deals with negative weights as well but djikastra cannot
- while we are doing bfs, we keep track of what is the minimum price of getting current node so far. 
- this is a bfs but till the end not just checking the neighbors
- If k stop, we will do k+1 layers of bfs. because problem states that between starting point and dest
- initially we are going to have min cost as infinity to reach other nodes. but start point's cost is 0
- 