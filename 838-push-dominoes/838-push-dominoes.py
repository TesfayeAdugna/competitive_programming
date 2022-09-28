class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        """
        .L.R...LR..L.. l = 0, r = 1
        
        LL.R...LR..L.. l = 0, r = 1
        LL.R...LR..L.. l = 1, r = 3
        LL.RR.LLR..L.. l = 3, r = 7
        LL.RR.LLRRLL.. l = 8, r = 11
        LL.RR.LLRRLL.. l = 11, r = 13
        5. ....L  -> all left           done
        3. L...L  -> all left           done
        
        1. R...L  ->  odd/even          done
        
        4. R...R  -> all right          done
        7. R....  -> all right          done

        6. ....R  -> do nothing
        2. L...R  -> do nothing
        8. L....  -> do nothing

        """
        dominoes = list(dominoes)
        l, r = 0, 1
        while r<len(dominoes)-1 and dominoes[r] == ".":
            r += 1
        
        while r < len(dominoes):
            if dominoes[l] != "R" and dominoes[r] == "L":
                while l <= r:
                    dominoes[l] = "L"
                    l += 1
            elif dominoes[l] == "R" and dominoes[r] != "L":
                while l <= r:
                    dominoes[l] = "R"
                    l += 1
            elif dominoes[l] == "R" and dominoes[r] == "L":
                left, right = l, r
                mid = (r+l)//2
                while l <= r:
                    if l < mid:
                        dominoes[l] = "R"
                    elif l > mid:
                        dominoes[l] = "L"
                    elif l == mid and (right-left) % 2 == 1:
                        dominoes[l] = "R"
                    l += 1
            l = r
            while l < len(dominoes)-1 and dominoes[l+1] != ".":
                l += 1
            r = l + 1
            while r<len(dominoes)-1 and dominoes[r] == ".":
                r += 1

        return "".join(dominoes)
    
    
    
    
    
    
