##This Solution was written before knowledge of Hashes

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            k = 1
            while i + k < len(nums):
                if nums[i]+ nums[(i+k)] == target:
                    return([i,(i+k)])
                k+=1

        
