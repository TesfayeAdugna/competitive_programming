class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        nums.sort()
        return nums
        # using merge sort - divide and conquer
#         def merge(left_arr, right_arr):
#             if not left_arr:
#                 return right_arr

#             if not right_arr:
#                 return left_arr

#             result = []
#             left_pointer, right_pointer = 0, 0
#             while len(result) < len(left_arr) + len(right_arr):
#                 if left_arr[left_pointer] <= right_arr[right_pointer]:
#                     result.append(left_arr[left_pointer])
#                     left_pointer += 1
#                 else:
#                     result.append(right_arr[right_pointer])
#                     right_pointer += 1

#                 if right_pointer == len(right_arr):
#                     result += left_arr[left_pointer:]
#                     break

#                 if left_pointer == len(left_arr):
#                     result += right_arr[right_pointer:]
#                     break
#             return result
        
        
        
#         if len(nums) <= 1:
#             return nums
        
#         mid = len(nums)//2
#         return merge(left_arr=self.sortArray(nums[:mid]), right_arr=self.sortArray(nums[mid:]))
    
    
    
    
    
    