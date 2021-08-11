from collections import defaultdict
from typing import List

class Solution():
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for str in strs:
            count=[0] * 26
            for s in str:
                count[ord(s)-ord("a")]+=1
            res[tuple(count)].append(str)
        return res.values()
    def faster(self,strs:List[List[str]])->List[list[str]]:
        res=[]
        group={}
        for str in strs:
            hashed=self.findHash(str)
            if hashed not in group:
                group[hashed]=[]
            group[hashed].append(str)
        for g in group.values():
            res.append(g)
        return res
    def findHash(self,s:str):
        return "".join(sorted(s))