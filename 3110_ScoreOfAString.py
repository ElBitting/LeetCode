class Solution:
    def scoreOfString(self, s: str) -> int:
        j = 0
        x = 0
        y = 0
        for j in range((len(s)-1)):
            x+=abs(ord(s[j]) - ord(s[(j+1)]))
        return(x)
