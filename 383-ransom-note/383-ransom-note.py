class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

        magazineL = []
        for c in magazine:
            magazineL.append(c)
        for c in ransomNote:
            if c in magazineL:
                magazineL.remove(c)
            else:
                return False
        return True