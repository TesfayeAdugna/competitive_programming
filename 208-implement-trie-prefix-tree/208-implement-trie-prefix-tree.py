class Node:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

        
class Trie:

    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        curr = self.node
        for char in word:
            if curr.children[ord(char)-ord('a')] == None:
                temp = Node()
                curr.children[ord(char)-ord('a')] = temp
            curr = curr.children[ord(char)-ord('a')]
            
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.node
        for char in word:
            if curr.children[ord(char)-ord('a')] == None:
                return False
            curr = curr.children[ord(char)-ord('a')]
            
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.node
        for char in prefix:
            if curr.children[ord(char)-ord('a')] == None:
                return False
            curr = curr.children[ord(char)-ord('a')]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)