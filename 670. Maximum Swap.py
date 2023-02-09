class Solution:
    def maximumSwap(self, num: int) -> int:

        to_str = num
        to_str = str(to_str)
        lst = [int(char) for char in to_str]
        if lst == sorted(lst, reverse=True) :
            return num
        dictionary = defaultdict(list) 
        for i,each in enumerate(lst) :
            dictionary[each].append(i)
        for i in range(len(lst)-1) :
            maxi=max(lst[i+1:])
            if lst[i]<maxi :
                ind=dictionary[maxi][-1]
                lst[i],lst[ind] = lst[ind],lst[i]
                break
        lst = [str(char) for char in lst]
        return int("".join(lst))
