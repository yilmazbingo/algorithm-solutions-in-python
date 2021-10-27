'''
133. Medium Clone Graph
Given a reference of a node in a connected undirected graph which is there is a path from any point to any other point in the graph.
Return a deep copy (clone) of the graph.
'''

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def clone(self,node):
        # we are mapping the old_node to the new node
        old_to_new={}
        # from start, we do till last item one way, when we react the last, we pop out and do the reverse
        def dfs(node):
            if node in old_to_new:
                # we return this and add it to the neighbors of the node
                return old_to_new[node]
            copy=Node(node.val)
            old_to_new[node]=copy
            # we are copyigh the neighbors array
            for nei in node.neighbors:
                # dfs(nei) will create the copy of the neighbor and we append it to the node's neighbors
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None