class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # we add each word in list to trie to create prefix tree
        for w in words:
            root.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        # res is set of words. it is possible we could visit same word twice inside the board
        res, visit = set(), set()

        # node is the current Node that we are at in trie depending on what chars we already visited before
        # word is what is word so far
        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children:
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)