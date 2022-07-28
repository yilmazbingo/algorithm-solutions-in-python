- It is a sort, returns a specific order of the vertexes of given graph, as long as graph satisfies certain conditions
- The only graphs that have valid topological ordering is called DIRECTED ACYCLIC GRAPH
- every tree has a topological ordering. since by definition, trees do not have any cycles. 

First thing we need to look at is a vertex in isolation. Every vertex in isolation has **Indegree** factor. THis only
applies as long as the vertex is within a Directed Acyclic Graph. Because if a graph is cyclic, there would be no vertex with the indegee of 0. because topological sort 
starts with the vertices whose indegree is 0. 


**Indegree Value:** It is essentially represented as how many connections are coming into this vertex. 

**Topological Sort:**
- It is a liner ordering of vertices such that for every directed edge UV(U->V), vertex U comes before vertex V in the ordering
- In the topological sort, you have to write first whichever comes first. Topological sort starts with the vertices 
whose indegree is 0. Vertices has outdefree value 0 comes last. 
- when you get a directed graph, you want to figure out what every vertex's indegree value. 
- the way that the topological sort works is that you can only take a vertex and its value as long as its indegree value is zero.
But once you take it, then you want to remove it from the graph. 
   This will reduce the indegree value of any nodes that it is directing into and then those nodes become open for us
to take as a next value. Because there may be multiple values where the indegree value is zer0, you can take them in whichever
order, it does not matter. Topological sort does not have a very set order as long as it follows these rules, there can be
multiple variations of the order for the same graph. 

- Aside building the adajcent list, we also have to build the indegree array. 
 
- It is always applicable in DAG, THERES SHOULD BE NO CYCLE. because, eventually we wont have any node whose indegree is 0 if it cyclic.
**Example**

prerequisites=[[1,0],[2,1],[2,5],[0,3],[4,3],[3,5],[4,5]]
# 0's -1 , 1's:1, 2's:2 ,3's:1, 4's:2, 5's:0
indegree_pre=[1,1,2,1,2,0]
adj_list=[[1],[2],[],[0,4],[],[2,3,4]]

- In the above example, only 5's indegree is 0. we remove 5 from indegree array and then update the indegree array.
We see if we remove 5, we reduce the indegree of the vertices that 5 was directed. % was directed to [2,3,4] so 
     
            indegree_pre=[1,1,1,0,1,"removed"]
            adj_list=[[1],[2],[],[0,4],[],"removed"]

Now we check if any of those indegee values is equal to zero. 3's indegree=0. Now we remove it, we look at the adj_list 
and see which vertices 3 is directed. `adj_list[3]=[0,4]`. reduce 0's and 4's 

            indegree_pre=[0,1,1,"removed",0,"removed"] 
            adj_list=[[1],[2],[],"removed",[],"removed"]

now 4's and 3's indegree is 0. we can go with either. 4 has no connected value in the adj list. 

           indegree_pre=[0,1,1,"removed","removed","removed"] 
           adj_list=[[1],[2],[],"removed","removed","removed"]

Check 0 now. 3 is connected to 1. reduce 1's indegree by 1
        
           indegree_pre=["removed",0,1,"removed","removed","removed"] 
           adj_list=["removed",[2],[],"removed","removed","removed"]

1's indegree is zero.

           indegree_pre=["removed","removed",0,"removed","removed","removed"] 
           adj_list=["removed","remmoved",[],"removed","removed","removed"]

This is how topological sort works. We have account for that all of these vertexes checked. if we do not touch
all the vertices that means we have a cycle. If we have a cycle in "course_schedule" problem, that means
courses cannot be completed so we return `False`