'''
There is only one entrance to this area, called root.
Besides the root, each house has one and only one parent house. After a tour, the smart
thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked
houses were broken into on the same night.
Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
'''

# We have two cases. 1 case with_root another case is without_root
# if we include the root, we have to skip the next level
# if we skip level, we can choose next level or we can even skip it if its child is greater. No restriction
# T: O(n) because we visit each node only one time.
#Time complexity: O(N) since we run the helper function for all nodes once, and saved the results to prevent the second calculation.
# Space complexity: O(N) since we need two maps with the size of O(N) to store the results, and O(N) space for stacks to start recursion.
from TreeNode import TreeNode

class Solution:
    def rob(self,root:TreeNode)->int:
        # returns pair [with_root,without_root]
        def dfs(root:TreeNode):
            if not root:
                return [0,0]
            left_pair=dfs(root.left)
            right_pair=dfs(root.right)
            # if we include root, we get the without_root of the returned pair which is the first index
            with_root=root.val+left_pair[1]+right_pair[1]
            # without_root has no restriction
            without_root=max(left_pair)+max(right_pair)
            return [with_root,without_root]
        return max(dfs(root))