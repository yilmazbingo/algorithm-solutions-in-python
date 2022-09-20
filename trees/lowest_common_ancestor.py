'''
236.Medium Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
# time complexity is the O(Log(n)) height of the tree. Because we are visiting only one node for each level
from TreeNode import TreeNode
'''
Time Complexity: O(N), where NN is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.

Space Complexity: O(N)O(N). This is because the maximum amount of space utilized by the recursion stack would be NN since the height of a skewed binary tree could be NN.


    - Start traversing the tree from the root node.
    - If the current node itself is one of p or q, we would mark a variable mid as True and continue the search for the other node in the left and right branches.
    - If either of the left or the right branch returns True, this means one of the two nodes was found below.
    - If at any point in the traversal, any two of the three flags left, right or mid become True, this means we have found the lowest common ancestor for the nodes p and q.
'''
class Solution:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        def recurse_tree(current_node):
            # If reached the end of a branch, return False.
            if not current_node:
                return False
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            # If the current node is one of p or q
            # this is actually the parent of left and right
            # each parent is asking its children if they include the one of the current
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node
            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans