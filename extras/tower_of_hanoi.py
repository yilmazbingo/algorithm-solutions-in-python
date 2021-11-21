
class Solution:
    def towerOfHanoi(self, n):
        res=[]
        # from,helper,to. there are 3 rods
        def hanoi(n,start,helper,dest):
            if n==0:
                return
            else:
                # first move it to h
                hanoi(n-1,start,dest,helper)
                res.append("from {} to {}".format(start, dest))
                hanoi(n-1,helper,start,dest)
        hanoi(n,"A","B","C")
        return res

