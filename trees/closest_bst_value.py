'''
https://www.lintcode.com/problem/900/
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
'''

# I think it must mention that bst eleements are positive

class Solution:
    def closestValue(self, root, target):
        diff = float("inf")
        # ans could be initialized with any value
        ans = target
        # we have to traverse entire tree. I used preorder traversal but any can work
        def preorder(root):
            if root:
                nonlocal diff
                diff = min(diff, abs(target - root.val))
                # this means diff has changed, so I update the ans
                if diff == abs(target - root.val):
                    nonlocal ans
                    ans = root.val
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ans
