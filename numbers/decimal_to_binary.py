

class Solution:
    def to_binary(self,n:int):
        if n==0:
            return '0'
        return self.to_binary(n//2)+str(n%2)