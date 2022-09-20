'''
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.
Return a string of the unique letters in the new alien language sorted in lexicographically increasing order.
    Input：["wrt","wrf","er","ett","rftt"]
    Output："wertf"
ape  apes
ape is prefix of apes so the order is ape < apes. If we get
     apes,ape
this is invalid.
- if we had   r=>t=>f and w=>e we have multiple solutions
'''
from typing import (List)
from collections import defaultdict, deque

class Solution:
    def alien_order(self, words: List[str]) -> str:
        in_degree = {ch: 0 for word in words for ch in word}
        # 1. Build graph
        graph = defaultdict(set)
        # zip is parallel iteration
        for w1, w2 in zip(words, words[1:]):
            for ch1, ch2 in zip(w1, w2):
                if ch1 != ch2:
                    if ch2 not in graph[ch1]:
                        graph[ch1].add(ch2)
                        in_degree[ch2] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(w2) < len(w1):
                    return ""
        print(graph)
        # 2. Identify vertices that have no incoming edge
        no_incoming_edges = deque([ch for ch in in_degree if in_degree[ch] == 0])

        # 3. Repeatedly pick vertex of in-degree 0 and append it to the output
        aliendict = ""
        while no_incoming_edges:
            vertex = no_incoming_edges.popleft()
            aliendict += vertex
            for ch in graph[vertex]:
                in_degree[ch] -= 1
                if in_degree[ch] == 0:
                    no_incoming_edges.append(ch)

        #         if len(aliendict) < len(in_degree):
        #             return ""

        return aliendict if len(aliendict) == len(in_degree) else ""


s = Solution()
s.alien_order(["wrt", "wrf", "er", "ett", "rftt"])