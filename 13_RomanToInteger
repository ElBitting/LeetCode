class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        key ={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
       
        solution = 0
        for j in range(len(s)):
            if j == 0:
                solution += key[s[j]]
            elif key[s[j]] >= key[s[(j-1)]]:
                solution += key[s[j]]
            else:
                solution -=key[s[j]]
        return(solution)
