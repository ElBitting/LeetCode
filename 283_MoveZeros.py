class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        counter = 0 
        while i < len(nums):
            if nums[i] ==0:
                nums.pop(i)
                counter +=1
            else:
                i+=1
        j = 0
        while j < counter:
            nums.append(0)
            j+=1

        
