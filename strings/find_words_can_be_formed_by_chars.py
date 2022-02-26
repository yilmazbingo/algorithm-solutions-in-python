'''
1160. Easy Find Words That Can Be Formed by Characters
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6 "cat" and "hat"
'''

# if you work with strings, consider converting strings into arrat
from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # making the string into an array to remove elements
        words_list=[list(x) for x in words]
        sum_array=[]
        for word in words_list:
            count=0
            chars_list=[char for char in chars]
            for letter in word:
                if letter in chars_list:
                    # this removes the first char if there is same char more than once
                    chars_list.remove(letter)
                    count+=1
            if len(word)==count:
                sum_array.append(len(word))
        return sum(sum_array)