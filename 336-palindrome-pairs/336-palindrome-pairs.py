class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        ans=[]
        dic = {word[::-1]: i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            if "" in dic and dic[""] != i and word== word[::-1]:
                ans.append([i, dic[""]])
            for j in range(1, len(word)+1):
                left= word[:j]
                right= word[j:]
                if left in dic and dic[left] != i and right == right[::-1]:
                    ans.append([i, dic[left]])
                if right in dic and dic[right] != i and left == left[::-1]:
                    ans.append([dic[right], i])
        return ans