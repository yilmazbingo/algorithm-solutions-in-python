#find the kth smallest element in bst.
# if we traverse bst in order and push each element to the array, we get sorted array.

# for iterative solution we need stack to store the visited node's values

class Solution:
    class Solution(object):
        def __init__(self):
            self.k = None
            self.res = None
        def kthSmallest(self, root, k):
            self.k = k
            def dfs(node):
                if not node:
                    return
                dfs(node.left)
                self.k -= 1
                if self.k == 0:
                    self.res = node.val
                    return self.res
                dfs(node.right)
            dfs(root)
            return self.res