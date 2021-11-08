'''
1- show f(1) works base case. if we have one disk put it to the end
2- Assume f(n-1) works
3- SHow f(n) works using f(n-1)
'''

class Solution:
    def towerOfHanoi(self, n):
        res=[]
        #
        def hanoi(n,start,med,end):
            if n==0:
                pass
            else:
                # Assume f(n-1) works move n-1 to the end
                hanoi(n-1,start,end,med)
                res.append("from {} to {}".format(start, end))
                hanoi(n-1,med,start,end)
        hanoi(n,"A","B","C")
        return res