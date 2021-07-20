# find the lowest common ancestor of two given nodes
# root is the common ancestor of every single node in the tree
# time complexity is the O(Log(n)) height of the tree. Because we are visiting only one node for each level

class Solution:
    def lowest(self,root:TreeNode,p:TreeNode,q:TreeNode):
        cur=root
        while cur:
            if p.val>cur.val and q.val>cur.val:
                cur=cur.right
            elif p.val<cur.val and q.val<cur.val:
                cur=cur.left
            else:
                return cur
