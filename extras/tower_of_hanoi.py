class Solution:

    def towerOfHanoi(self, n):
        res=[]
        def move(f,t):
            res.append("from {} to {}".format(f,t))
        # from,helper,to
        def hanoi(n,f,h,t):
            if n==0:
                pass
            else:
                hanoi(n-1,f,t,h)
                move(f,t)
                hanoi(n-1,h,f,t)
        hanoi(n,"A","B","C")
        return res

