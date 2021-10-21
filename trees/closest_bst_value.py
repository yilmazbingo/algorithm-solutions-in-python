'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
'''

# I think it must mention that bst eleements are positive

class Solution:
    def closestValue(self, root, target):
        diff = float("inf")
        ans = target
        # we have to traverse entire tree. I used preorder traversal but any can work
        def dfs(root):
            if root:
                nonlocal diff
                diff = min(diff, abs(target - root.val))
                if diff == abs(target - root.val):
                    nonlocal ans
                    ans = root.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return ans
