# Given a reference of a node in CONNECTED UNDIRECTED graph, return a deep copy of graph

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def clone(self,node):
        old_to_new={}
        # from start, we do till last item one way, when we react the last, we pop out and do the reverse
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            # we just copied the value
            copy=Node(node.val)
            old_to_new[node]=copy
            # we are copyigh the neighbors array
            for nei in node.neighbors:
                # dfs(nei) will create the copy of the neighbor and we append it to the node's neighbors
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None