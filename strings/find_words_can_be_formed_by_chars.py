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
        words_list = [list(x) for x in words]  # making the string into an array to remove elements
        sum_array = []  # to store the final length of all the substrings formed
        for word in words_list:
            count = 0
            # for each word, after deletion we should hava reinitiaated the chars_list
            chars_list = [char for char in chars]
            for char in word:
                if char in chars_list:
                    chars_list.remove(char)
                    count += 1
            if count == len(word):
                sum_array.append(len(word))
        return sum(sum_array)