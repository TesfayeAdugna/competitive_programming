"""
https://leetcode.com/problems/implement-trie-prefix-tree/
"""

class Node:
    def __init__(self):
        self.child = [None]*26
        self.isWord = False
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            index = ord(c)-ord('a')
            if current.child[index] is None: 
                current.child[index] = Node()
            current = current.child[index]
        current.isWord = True
        
    def search(self, word: str, isPrefix: bool = False) -> bool:
        current = self.root
        for c in word:
            index = ord(c)-ord('a')
            if current.child[index] is None: 
                return False
            current = current.child[index]
        if current.isWord or isPrefix:
            return True
        return False
    
    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)