class Solution:
    def recursive(self,s:str):
        string=''.join(char.lower() for char in s if char.isalnum())
        def dfs(s:str):
            if len(s)<=1:
                return True
            if s[0]==s[-1]:
                return dfs(s[1:-1])
            return False
        return dfs(string)
s=Solution()
print(s.recursive("aba"))
