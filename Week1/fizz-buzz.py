class Solution(object):
    def fizzBuzz(self, n):
        """
        https://leetcode.com/problems/fizz-buzz/submissions/]
        """
        empty = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                empty.append("FizzBuzz")
            elif i%3==0:
                empty.append("Fizz")
            elif i%5==0:
                empty.append("Buzz")
            else:
                empty.append(str(i))
        return empty