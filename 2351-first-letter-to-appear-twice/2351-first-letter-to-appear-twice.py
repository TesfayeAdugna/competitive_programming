class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        
        
        
        
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
                if count[char] == 2:
                    return char
            else:
                count[char] = 1
