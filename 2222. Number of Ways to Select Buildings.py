class Solution:
    def numberOfWays(self, s: str) -> int:

        current_1, current_0, total_1, total_0, result, n = 0, 0, 0, 0, 0, len(s)
        
        for bit in s:
            if bit == '1':
                total_1 += 1
            else:
                total_0 += 1
        
        if s[0] == '0': current_0 += 1
        else: current_1 += 1
			
        for i in range(1, n - 1):
            if s[i] == '0':
                current_0 += 1
                result += current_1 * (total_1 - current_1)
            else:
                current_1 += 1
                result += current_0 * (total_0 - current_0)
                
        return result
