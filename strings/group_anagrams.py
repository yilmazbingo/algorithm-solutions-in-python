'''
49. Medium Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
from collections import defaultdict
from typing import List

# T:O(m*n)
class Solution():
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # "eat", key will be "1e,1a,1t", values will be ["eat","tea","ate"]
        res=defaultdict(list)
        for string in strs:
            # count each string how many letters they have. [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            count=[0] * 26
            for s in string:
                # finding the index of chars in alphabet. take asci value of each char and substract asci value of "a".
                count[ord(s)-ord("a")]+=1
            # list cannot be keys, so we change it to tuple
            res[tuple(count)].append(string)
        return res.values()


    def faster(self,strs:List[List[str]])->List[list[str]]:
        res=[]
        group={}
        for str in strs:
            hashed=self.findHash(str)
            # I could use default dict
            if hashed not in group:
                group[hashed]=[]
            group[hashed].append(str)
        for g in group.values():
            res.append(g)
        return res
    def findHash(self,s:str):
        return "".join(sorted(s))