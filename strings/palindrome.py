


class Solution:
    # this is very slow but works
    def recursive(self,s:str):
        string=''.join(char.lower() for char in s if char.isalnum())
        def dfs(s:str):
            if len(s)<=1:
                return True
            if s[0]==s[-1]:
                return dfs(s[1:-1])

        return dfs(string)

