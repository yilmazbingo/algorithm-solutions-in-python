'''
1160. Easy Find Words That Can Be Formed by Characters
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
'''

# if you work with strings, consider converting strings into arrat
from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        arr = [list(x) for x in words]  # making the string into an array to remove elements

        sum_array = []  # to store the final length of all the substrings formed
        for i in arr:
            count = 0
            f = [char for char in chars]
            for j in i:
                if j in f:
                    f.remove(j)
                    count += 1
            if count == len(i):
                sum_array.append(len(i))
        return sum(sum_array)