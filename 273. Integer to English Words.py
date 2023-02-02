class Solution:
    def numberToWords(self, num: int) -> str:
        
        digit_name = {0:"Zero",
                     1:"One",
                     2:"Two",
                     3:"Three",
                     4:"Four",
                     5:"Five",
                     6:"Six",
                     7:"Seven",
                     8:"Eight",
                     9:"Nine",
                     10:"Ten",
                     11:"Eleven",
                     12:"Twelve",
                     13:"Thirteen",
                     14:"Fourteen",
                     15:"Fifteen",
                     16:"Sixteen",
                     17:"Seventeen",
                     18:"Eighteen",
                     19:"Nineteen",
                     20:"Twenty",
                     30:"Thirty",
                     40:"Forty",
                     50:"Fifty",
                     60:"Sixty",
                     70:"Seventy",
                     80:"Eighty",
                     90:"Ninety",
                     100:"Hundred",
                     1000:"Thousand",
                     1000000:"Million",
                     1000000000:"Billion"
        }

        if num == 0: return digit_name[num]

        output, group, factor = [], 0, 3
        g_div, g_mod = divmod(num, 1000)
        
        while g_div or g_mod:
            if g_mod and group:
                output.append(digit_name[pow(1000, group)])
            div = g_mod
            i = 0
            while i < factor:
                if (div == g_mod) and (11 <= div % 100 <= 19):
                    output.append(digit_name[div%100])
                    div = div // 100
                    i += 2
                else:
                    div, mod = divmod(div, 10)
                    if mod:
                        if not i:
                            output.append(digit_name[mod])
                        elif i == 1:
                            output.append(digit_name[mod*10])
                        elif i == 2:
                            output.append(digit_name[100])
                            output.append(digit_name[mod])
                    i += 1

            g_div, g_mod = divmod(g_div, 1000)
            group += 1

        return " ".join(reversed(output))
            
