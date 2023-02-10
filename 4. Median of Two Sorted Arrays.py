class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = []
        index1, index2 = 0, 0
        while index1 < len(nums1) or index2 < len(nums2):
            if index1 >= len(nums1):
                mergedList.append(nums2[index2])
                index2 += 1
            elif index2 >= len(nums2):
                mergedList.append(nums1[index1])
                index1 += 1
            
            elif nums1[index1] <= nums2[index2]:
                mergedList.append(nums1[index1])
                index1 += 1
            else:
                mergedList.append(nums2[index2])
                index2 += 1

        n = len(mergedList)
        if n%2 == 0:
            first, second = n//2-1, n//2
            return (mergedList[first]+mergedList[second])/2
        else:
            return mergedList[n//2]
            
        







