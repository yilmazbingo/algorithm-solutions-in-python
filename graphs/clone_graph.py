'''
133. Medium Clone Graph
Given a reference of a node in a connected undirected graph which is there is a path from any point to any other point in the graph.
Return a deep copy (clone) of the graph.
'''
# T:O(n)=E+V
# In graph problems makse sure do not visit the same node
from collections import deque
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        queue = deque()
        # this will be holding the graph copy
        clones = {}
        clones[node] = Node(node.val, [])
        queue.append(node)
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                # we are appending the reference of clones[neighbor] not creating a new value
                clones[current].neighbors.append(clones[neighbor])
        return clones[node]

    def clone(self, node):
        # we are using mapping to handle the relationship of node and its neighbors
        old_to_new = {}

        # from start, we do till last item one way, when we reach the last, we pop out and do the reverse
        def dfs(node):
            if node in old_to_new:
                # we return this and add it to the neighbors of the node. this is where we create it arrow into the node.  <--
                return old_to_new[node]
            copy = Node(node.val)
            old_to_new[node] = copy
            # we are copyigh the neighbors array
            for nei in node.neighbors:
                # dfs(nei) will create the copy of the neighbor and we append it to the node's neighbors
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
