


class Solution:
    def edit(self,word1:str,word2:str)->int:
        store = [[float('inf')] * (len(word2) + 1) for j in range(len(word1) + 1)]
        #     print(store)

        for i in range(len(word2) + 1):
            store[len(word1)][i] = len(word2) - i
        for j in range(len(word1) + 1):
            store[j][len(word2)] = len(word1) - j
        print(store)
        for i in range(len(word2)-1, -1, -1):
            for j in range(len(word1)-1, -1, -1):
                if word1[i] == word2[j]:
                    store[i][j] == store[i + 1][j + 1]
                else:
                    store[i][j] = 1 + min(store[i + 1][j + 1], store[i][j + 1], store[i + 1][j])

        return store[0][0]


s=Solution()
print(s.edit("abc","abd"))