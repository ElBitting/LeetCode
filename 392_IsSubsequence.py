class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t_list = list(t)
        n = 0

        j = 0
        for i in range(len(s)):
            if s[i] in t_list:
                n = t_list.index(s[i])
                j=0
                while j <= n:
                    t_list.pop(0)
                    j +=1
                i +=1
            else:
                return(False)
            

        print(t_list)
        return(True)
