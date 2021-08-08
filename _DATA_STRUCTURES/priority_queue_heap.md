- A priority queuw is an Abstract Data type that operates similar to a normal queue except that each element 
  in the priority queue has a certain priority. the priority of the elements in the priority queue determine the order
  in which elements are removed from the PQ.
  
- Priority queues only supports comparable data. 

**Examples**
Let's say passengers book tickets for the train. Once the capacity is full, then later bookings are in an awaiting list 
according to the firs come basis. But maybe another company priorities the senior passengers in the awaiting list.

## Heaps
Heap data structure is more efficient utilization of priority queues. Using heap structure we can perform both
insertion and deletion in a much better way. Heaps are priority queues which store collection of elements, but
the elements are stored using binary tree. Therefore Heaps are known as Binary Heaps. 

There are two additional properties with heaps: 
 - Relational property which defined how the elements' keys are stored.  Max heap or Min heap
 - Structural property which defines the shape of the binary tree in which elements' keys are stored. It should be 
a complete Binary tree.
    
   Complete binary trees are ones where every single level is full, except for the very last level. if there are nodes in the last level, it must be as pushed to the left possible.

## heapq
this module supports for operations that can be performed on heaps, which are priority queues. This module works on 
list object. Elements are stored in a list which starts from index 0. 0the element will contain the smallest element of the heap.
`heapq` basically creates a mini heap using the element stored in the list.

```py
import heapq as heap

L1=[]
heap.heappush(L1,25)
heap.heappush(L1,2)
heap.heappush(L1,21)

a=heap.heappop(L1)
print(a)
print(L1) # [2,21,25)
```