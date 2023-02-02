class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:


        letter_logs, digit_logs = [], []
        
        for log in logs:
            
            tmp = log.split(" ")
            
            if tmp[1].isalpha(): letter_logs.append(tmp)

            else: digit_logs.append(tmp)
                
        
        letter_logs.sort(key = lambda x: (x[1:],x[0]))
        
        result = []
        for log in letter_logs:
            result.append(" ".join(log))
        for log in digit_logs:
            result.append(" ".join(log))

        return result
