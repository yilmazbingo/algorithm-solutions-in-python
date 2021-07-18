# serialize with preorder

from treetoy import TreeNode
class Codec:
    def serialize(self,root:TreeNode):
        res=[]
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self,data):
        values=data.split(",")
        self.i=0
        def dfs():
            if values[i]=="N":
                self.i+=1
                return None
            node=TreeNode(int(values[self.i]))
            # if it is not "N", we still have to increase the index
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()