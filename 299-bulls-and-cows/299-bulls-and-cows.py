class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        c = Counter(secret)
        bull = 0
        cow = 0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bull += 1
                if c[guess[i]] > 0:
                    c[guess[i]]-=1
                else:
                    cow -= 1
            elif guess[i] in c and c[guess[i]]>0:
                c[guess[i]] -= 1
                cow += 1
                    
        return str(bull) + "A" + str(cow) + "B"