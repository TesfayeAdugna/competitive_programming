class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        
        dic = {
            'a': ".-",
            'b': "-...",
            'c': "-.-.",
            'd': "-..",
            'e': ".",
            'f': "..-.",
            'g': "--.",
            'h': "....",
            'i': "..",
            'j': ".---",
            'k': "-.-",
            'l': ".-..",
            'm': "--",
            'n': "-.",
            'o': "---",
            'p': ".--.",
            'q': "--.-",
            'r': ".-.",
            's': "...",
            't': "-",
            'u': "..-",
            'v': "...-",
            'w': ".--",
            'x': "-..-",
            'y': "-.--",
            'z': "--..",
        }
        
        Answer = set()
        for word in words:
            temp = []
            for char in word:
                temp.append(dic[char])
            
            Answer.add("".join(temp))
        return len(Answer)
        
        
        
        
        
        
        