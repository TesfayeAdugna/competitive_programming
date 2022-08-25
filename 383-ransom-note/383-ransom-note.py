class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        
        ransom = Counter(ransomNote)
        magazin = Counter(magazine)
        
        for key in ransom:
            if key not in magazin or magazin[key] < ransom[key]:
                return False
        return True