# A binary tree's max depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Since we are traversing entire tree, time complexity is O(N).
# Memory complexity will be the height of the tree, which can be O(N) if it is not balanced binary tree

#bfs assumes that node that we are looking for is closer to the root.
#------------------- RECURSION ---------------
class Solution:
    #dfs assumes no
    def max_depth(self,root):
        if not root:
            return 0
        return 1+max(self.max_depth(root.left),self.max_depth(root.right))

#------------------ BREADTH FIRST SEARCH -------------
import collections
class Solution:
    def max_depth(self,root):
        if not root:
            return 0
        level=0
        q=collections.deque([root])
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level

#-------------------- ITERATIVE DEPTH SEARCH ---------------------
class Solution:
    def max_depth(self,root):
        stack=[[root,1]]
        res=0
        while stack:
            node,depth=stack.pop()
            if node:
                res=max(res,depth)
                # node.left or node.right mighg be null. thats why we check if node:
                stack.append([node.left,depth+1])
                stack.append(node.right,depth+1)
        return res