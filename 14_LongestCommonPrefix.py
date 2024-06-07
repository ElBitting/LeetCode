class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key = len)

        solution = ''
        n = ''
        for i in range(len(strs[0])):
            n = strs[0][i]
            counter = 0
            for j in range(len(strs)):
                if n == strs[j][i]:
                    counter+=1
            if counter == len(strs):
                solution +=strs[0][i]
            else:
                break
            
        return(solution)
