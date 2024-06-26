class Solution:
    def sortColors(self, nums: List[int]) -> None:
        dic = Counter(nums)
        i, k = 0,0 
        for color in range(3):
            while i < dic[color]:
                nums[k] = color
                k+=1
                i+=1
            i = 0
