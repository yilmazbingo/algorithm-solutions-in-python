# Implement a trie with insert,search and startsWith
class TrieNode:
    def __init__(self):
        # each key is a TrieNode
        self.keys = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    # insert(self, word: str, node=this.root) node=this.root gives error "this" is not defined
    def insert(self, word: str, node=None) -> None:
        if node == None:
            node = self.root
        # insertion is a recursive operation
        if len(word) == 0:
            node.end = True
            return
        elif word[0] not in node.keys:
            node.keys[word[0]] = TrieNode()
            self.insert(word[1:], node.keys[word[0]])
        # that means key exists
        else:
            self.insert(word[1:], node.keys[word[0]])
    def search(self, word: str, node=None) -> bool:
        if node == None:
            node = self.root
        # node.end=True means we have inserted the word before
        if len(word) == 0 and node.end == True:
            return True
        # if we inserted apple and then search for app we get false becase we never inserted app so a-p-p last_p.end is not True
        # But startsWith(app) would return True
        elif len(word) == 0:
            return False
        elif word[0] not in node.keys:
            return False
        else:
            # we have to return becasue api expects us to return bool
            return self.search(word[1:], node.keys[word[0]])

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
# this will return false becasue a-p-p last p has no end. we did not insert app
trie.search("app");
trie.startsWith("app");
trie.insert("app");
trie.search("app"); 


