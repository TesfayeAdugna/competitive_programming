class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:

        def dfs(freq, path, result):
            if not freq:  
                result.append(path)
                return 

            for i in list(freq.keys()):
                if not path:
                    if freq[i] == 1:
                        del freq[i]
                    else:
                        freq[i] -= 1

                    dfs(freq,path+[i],result)
                    freq[i] += 1

                else:
                    if freq[i] == 1:
                        del freq[i]
                    else:
                        freq[i] -= 1
                    if int((i + path[-1])**(0.5)) == (i+path[-1])**(0.5):
                        dfs(freq, path + [i], result)
                    freq[i] += 1
        path = []
        result = []
        dfs(Counter(nums), path, result)
        return len(result)
