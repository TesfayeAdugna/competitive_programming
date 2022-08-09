class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        total_nums = len(arr)
        modulo = 10**9 + 7
        count_product_dict = {num: 1 for num in arr}
        arr.sort()

        for i in range(1, total_nums):
            for j in range(i):
                quotient = arr[i] // arr[j]
                if quotient < 2 or math.sqrt(arr[i]) > arr[i- 1]:
                    break
                if arr[i] % arr[j] == 0:
                    count_product_dict[arr[i]] += count_product_dict[arr[j]] * count_product_dict.get(quotient, 0)
                    count_product_dict[arr[i]] %= modulo
                    
        return sum(count_product_dict.values()) % modulo