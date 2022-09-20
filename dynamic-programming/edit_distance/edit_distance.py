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
    def minDistance(self, word1: str, word2: str) -> int:
        store = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # storing the base case. store[m+1][m+1] will be 0 when both are ""
        # converting "abc" to "" delete all. converting "" to "abc" insert all, "" to "" is 0.
        for i in range(len(word2) + 1):
            store[len(word1)][i] = len(word2) - i
        for j in range(len(word1) + 1):
            store[j][len(word2)] = len(word1) - j
        # bottom up approach, because if we start from beggininig, result would be depend on the sub problem so we start from sub problem
        # if chars are equal we dont do any operation.
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    # if letters are equal, we forward the indices and number of operation is 0
                    store[i][j] = store[i + 1][j + 1]
                else:
                    # min operation is replace
                    # word1=abd, word2=acd     replace             inserting         deleting
                    # if we insert "c" to "abd" when i is at "b". pointer will still at b(acbd). but we handled "C, so we move j by 1 store[i][j + 1]
                    # if I delete "b" from word1, I will shift the "i", but j will remain because we are looking for its mathc store[i + 1][j])
                    # if we replace, means we handle the chars in both words so we move forward.
                    store[i][j] = 1 + min(store[i + 1][j + 1], store[i][j + 1], store[i + 1][j])
        return store[0][0]

s=Solution()
print(s.edit("abc","abd"))