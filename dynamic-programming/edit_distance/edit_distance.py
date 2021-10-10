'''
72. Hard Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character. Change one char into another
'''
# we need to create patter for each operation
class Solution:
    def edit(self,word1:str,word2:str)->int:
        store = [[float('inf')] * (len(word2) + 1) for j in range(len(word1) + 1)]
        for i in range(len(word2) + 1):
            store[len(word1)][i] = len(word2) - i
        for j in range(len(word1) + 1):
            store[j][len(word2)] = len(word1) - j
        print(store)
        # bottom up approach, because starting from base case.
        for i in range(len(word2)-1, -1, -1):
            for j in range(len(word1)-1, -1, -1):
                # if chars are equal we dont do any operation.
                if word1[i] == word2[j]:
                    store[i][j] == store[i + 1][j + 1]
                else:
                    #                       replace             inserting         deleting
                    store[i][j] = 1 + min(store[i + 1][j + 1], store[i][j + 1], store[i + 1][j])
        return store[0][0]


s=Solution()
print(s.edit("abc","abd"))