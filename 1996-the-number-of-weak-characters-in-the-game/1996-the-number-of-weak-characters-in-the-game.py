class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        
        
        dic={}

        for key,val in properties:
            if key in dic:
                dic[key].append(val)
            else:
                dic[key]=[val]

        weak=0
        max_defense=0

        for attack in sorted(dic.keys(), reverse=True):
            for defense in dic[attack]:
                if defense<max_defense:
                    weak+=1
            max_defense=max(max_defense,max(dic[attack]))

        return weak