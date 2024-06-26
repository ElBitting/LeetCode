class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        top = m -1
        bot = n -1
        k =  n + m - 1

        while bot >= 0:
            if top >= 0 and nums1[top] > nums2[bot]:
                nums1[k] = nums1[top]
                top -=1
            else:
                nums1[k] = nums2[bot]
                bot -=1
            k-=1
