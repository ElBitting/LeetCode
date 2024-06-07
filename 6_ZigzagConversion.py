class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1 or numRows> len(s):
            return(s)
        zigzag = [''] * numRows 
        j= 0
        i=0
        while i < len(s):
                while j < numRows and i < len(s):
                    zigzag[j] = zigzag[j]+s[i]
                    j+=1
                    i+=1
                j-=1
                while j > 0 and i < len(s):
                    j -=1
                    zigzag[j] += s[i]
                    i +=1
                j+=1
        Final = ''
        for k in range(numRows):
            Final += zigzag[k]
        return(Final)
