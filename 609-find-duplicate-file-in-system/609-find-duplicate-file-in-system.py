class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for path in paths:
            temp = path.split()
            for i in range(1, len(temp)):
                file = temp[i].split(".")
                file_path = file[0]
                file_name = file[1]
                file_content = file_name[4:-1]
                dic[file_content].append(temp[0]+"/"+file_path+"."+file_name[:3])
        answer = []
        for key in dic:
            if len(dic[key]) > 1:
                answer.append(dic[key])
        return answer