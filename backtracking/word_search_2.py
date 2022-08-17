from typing import Optional,List
class TrieNode:

    def __init__(self, val: str = None, parent: Optional['TrieNode'] = None):
        self.children = {}
        self.val = val
        self.parent = parent
        self.word = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(val=c, parent=node)
            node = node.children[c]
        node.word = word

    def prune(self, node: TrieNode) -> None:
        """
        When a word is found, we will perform the following actions:

        - Set the word node's "word" to None
        - If the current word node's child count is 0, we will
          traverse up node's parent and "evict" the child. We will
          perform this check up to trie until we reach a node who's child
          count is not zero OR we are at the root

        The reason why we do this is because we only need to match
        a word once. So we will improve subsequent word searches by
        pruning branches to words we've already found. We always check if
        a node's child count is 0 because we don't want to prune
        a branch if there are still words further down.

        For example:

            "bat", "batter", "battery"

        If we found "bat", then "bat" is no longer an eligible word.
        However, "batter" and "battery" are both further down the
        trie, so we don't prune this branch yet.

        If we found "battery" next, then this branch would be pruned
        to "bat", "batter".

        Finally, after finding "batter", we will prune the entire
        "bat..." branch.
        """
        # remove current word from possible match later
        node.word = None

        # prune trie until we reach a node with remaining children
        # or the root
        child = node
        parent = child.parent
        while parent and len(child.children) == 0:
            del parent.children[child.val]
            child = parent
            parent = parent.parent


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        res = []
        m, n = len(board), len(board[0])
        seen = set()

        def dfs(i, j, node) -> None:
            if (i < 0 or i == m or j < 0 or j == n or
                    (i, j) in seen or board[i][j] not in node.children):
                return

            # we can use current board position to (maybe) build a word
            seen.add((i, j))
            node = node.children[board[i][j]]

            if node.word:
                res.append(node.word)
                trie.prune(node)

            if len(node.children) == 0:
                # no more words can be built from here
                # no need to dfs further, so we backtrack
                seen.remove((i, j))
                return

            dfs(i + 1, j, node)
            dfs(i - 1, j, node)
            dfs(i, j + 1, node)
            dfs(i, j - 1, node)

            # back track
            seen.remove((i, j))

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)

        return res

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isWord = False
#
#     def add_word(self, word):
#         cur = self
#         for letter in word:
#             if letter not in cur.children:
#                 cur.children[letter] = TrieNode()
#             cur = cur.children[letter]
#         cur.isWord = True
#
# from typing import List
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         root = TrieNode()
#         # we add each word in list to trie to create prefix tree
#         for w in words:
#             root.add_word(w)
#
#         ROWS, COLS = len(board), len(board[0])
#         # res is set of words. it is possible we could visit same word twice inside the board
#         res, visit = set(), set()
#
#         # node is the current Node that we are at in trie depending on what chars we already visited before
#         # word is what is word so far
#         def dfs(r, c, node, word):
#             # board[r][c] not in node.children means we are on a letter that does not even exists in words list
#             if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children:
#                 return
#             visit.add((r, c))
#             node = node.children[board[r][c]]
#             word += board[r][c]
#             if node.isWord:
#                 res.add(word)
#             dfs(r - 1, c, node, word)
#             dfs(r + 1, c, node, word)
#             dfs(r, c - 1, node, word)
#             dfs(r, c + 1, node, word)
#
#             visit.remove((r, c))
#
#         for r in range(ROWS):
#             for c in range(COLS):
#                 dfs(r, c, root, "")
#         return list(res)