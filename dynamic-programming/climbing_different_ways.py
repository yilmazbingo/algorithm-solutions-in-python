# eacht time you can climb 1 or twice
#similar to fibonacci

# Butoom up soluiton
# create dp and start from the end. from end and previous, there is only one way to reach top
class Solution:
    def stairs(self,n):
        one,two=1,1
        for i in range(n-1):
            temp=one+two
            one=two
            two=temp
        return temp