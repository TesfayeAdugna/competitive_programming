class Node:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
        self.word = ""
        
class Solution:
    def __init__(self):
        self.node = Node()
    
    def insert(self, word: str) -> None:
        current = self.node
        for i,char in enumerate(word):
            if current.children[ord(char)-ord('a')] == None:
                current.children[ord(char)-ord('a')] = Node()
            current = current.children[ord(char)-ord('a')]
            if i == len(word)-1:
                current.word = word
        current.isEnd = True
                
    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.insert(word)
        
        current = self.node
        self.answer = ""
        def helper(node):
            if node.isEnd==True:
                if len(node.word) > len(self.answer):
                    self.answer = node.word
            if node.isEnd==False:
                return
            
            for child in node.children:
                if child != None:
                    helper(child)
        
        for curr in current.children:
            if curr != None:
                helper(curr)
                
        return self.answer
        
        
        
        
        
        
        