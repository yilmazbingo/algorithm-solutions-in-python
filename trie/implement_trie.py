class TrieNode:
    def __init__(self):
        self.keys = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str, node=None) -> None:
        if node == None:
            node = self.root
        if len(word) == 0:
            node.end = True
            return
        elif word[0] not in node.keys:
            node.keys[word[0]] = TrieNode()
            self.insert(word[1:], node.keys[word[0]])
        else:
            self.insert(word[1:], node.keys[word[0]])
   # returning bool so we have to return the recursive function
    def search(self, word: str, node=None) -> bool:
        if node == None:
            node = self.root
        if len(word) == 0 and node.end == True:
            print("yilma")
            return True
        elif len(word) == 0:
            return False
        elif word[0] not in node.keys:
            return False
        else:
            return self.search(word[1:], node.keys[word[0]])

    # returning bool so we have to return the recursive function
    def startsWith(self, prefix: str, node=None) -> bool:
        if node == None:
            node = self.root
        if len(prefix) == 0:
            return True
        elif prefix[0] not in node.keys:
            return False
        else:
            return self.startsWith(prefix[1:], node.keys[prefix[0]])


trie = Trie();
trie.insert("apple");
trie.search("apple");
trie.search("app");
trie.startsWith("app");
trie.insert("app");
trie.search("app"); 


