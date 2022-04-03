# 431 · Connected Component in Undirected Graph
# returns the values of each component

class Solution:
    def connectedSet(self, nodes):
        res = []
        visited = set()
        def dfs(node, path):
            path.append(node.label)
            visited.add(node)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    dfs(neighbor, path)
        for node in nodes:
            if node not in visited:
                path = []
                dfs(node, path)
                # question should have mention that it should be sorted
                res.append(sorted(path.copy()))
        return res
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