class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        final =[]
        dic = Counter(arr1)
        x = 0
        for num in arr2:
            final.extend([num]*dic[num])
            del(dic[num])
        temp = sorted(dic)

        for num in temp:
            final.extend([num]*dic[num])

        return final
