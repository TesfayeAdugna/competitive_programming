class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        :https://leetcode.com/problems/k-closest-points-to-origin/submissions/
        """
        newarray = []
        for i in range(len(points)):
            newarray.append(points[i][0]**2 + points[i][-1]**2)
        newar = sorted(newarray)
        newar2 = newar[:k]
        maximum = newar2[k-1]
        newarray2 = []
        for j in range(len(points)):
            if (points[j][0]**2 + points[j][1]**2)<=maximum:
                newarray2.append(points[j])
        newarray3 = newarray2[:k]
        return newarray3
            