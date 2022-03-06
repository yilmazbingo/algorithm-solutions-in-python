# 431 · Connected Component in Undirected Graph
# returns the values of each component
class Solution:
    def connectedSet(self, nodes):
        res, seen = [], set()
        def dfs(node):
            seen.add(node)
            connected = [node.label]
            for neighbor in node.neighbors:
                if neighbor not in seen:
                    connected += dfs(neighbor)
            return connected
        for node in nodes:
            if node not in seen:
                res.append(sorted(dfs(node)))
        return res