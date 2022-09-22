class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic, answer = defaultdict(int), []
        if len(s)<10: return []
        
        for i in range(len(s)):
            if i+9 < len(s): last = i+10
            else: last = len(s)-1
                
            DNASequence = s[i:last]
            dic[DNASequence]+=1

        for DNAsequence in dic:
            if DNAsequence != '' and dic[DNAsequence]>1:
                answer.append(DNAsequence)

        return answer
    