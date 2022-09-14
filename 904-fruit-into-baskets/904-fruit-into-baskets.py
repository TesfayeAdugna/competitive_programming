class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        
        
        
        left, right, maxFruit, fruitType = 0, 0, 0, defaultdict(int)
        while right < len(fruits):
            if len(fruitType) <= 1 or fruits[right] in fruitType:
                fruitType[fruits[right]], right = fruitType[fruits[right]]+1, right+1
            else:
                fruitType[fruits[left]] -= 1
                if fruitType[fruits[left]] == 0: del fruitType[fruits[left]]
                left += 1
            maxFruit = max(maxFruit, right-left)
        return maxFruit