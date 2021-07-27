# Given a reference of a node in connected undirected graph, return a deep copy of graph

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def clone(self,node):
        old_to_new={}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            # we just copied the value
            copy=Node(node.val)
            old_to_new[node]=copy
            # we are copyigh the neighbors array
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None