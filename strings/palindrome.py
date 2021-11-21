


class Solution:
    def recursive(self,s:str):
        string=''.join(char.lower() for char in s if char.isalnum())
        def dfs(s:str):
            if len(s)<=1:
                return True
            if s[0]==s[-1]:
                #reduce the bigger problem to smaller problem
                return dfs(s[1:-1])
        return dfs(string)

