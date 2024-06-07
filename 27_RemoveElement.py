class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        nums1 =[]
        m = len(nums)
        i = 0                            #place spot

        while i < m:
            if nums[i] == val:
                i +=1
            else:
                nums1.append(nums[i])
                i+=1
                
        nums[:] = nums1[:]
