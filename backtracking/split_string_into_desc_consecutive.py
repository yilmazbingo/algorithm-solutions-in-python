


class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index,prev):
            if index==len(s):
                return True
            for j in range(index,len(s)):
                val=int(s[index:j+1])
                # we are not looking for only 1 substring, look for all substrings
                # val+1==prev  is pruning. that's make algorithm more efficient cause if not true, it does not dfs()
                if val+1==prev and dfs(j+1,val):
                    return True
            # if we get here, means we could not split the string
            return False
        # determine the first integer. we have to split it at least by 2
        for i in range(len(s)-1):
            # there is no restriction what first value be
            val=int(s[:i+1])
            if dfs(i+1,val): return True
        return False