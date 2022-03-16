'''
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a
string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily
need to follow this format, so please be creative and come up with different approaches yourself.

'''
from TreeNode import TreeNode
class Codec:
    def __init__(self):
        self.i=0
    def serialize(self,root:TreeNode):
        res=[]
        def preorder(node):
            if not node:
                # N is for null means node has no child
                res.append("N")
                return
            #PREORDER  T:O(N) S:O(N)
            res.append(str(root.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(res)

    def deserialize(self,data):
        values=data.split(",")
        def dfs():
            if values[self.i]=="N":
                self.i+=1
                return None
            # since we serialized as preorder in which first element is the node
            node=TreeNode(int(values[self.i]))
            # if it is not "N", we still have to increase the index
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()