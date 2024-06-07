class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = list(s)
        s = sorted(s)
        s = sorted(s, key = s.count,
                                reverse = True)
        counter = 1
        
        i = 0
        evencounter = 0
        n = len(s)

        while i < n:
            if s.count(s[i])%2 == 0:
                evencounter +=s.count(s[i])
                counter += s.count(s[i])
                i += s.count(s[i])
            else:
                if s.count(s[i]) == n:
                    counter = n
                    i = n
                else:
                    counter += (s.count(s[i])-1)
                    i +=s.count(s[i])
        
        if evencounter == n:
            counter =n

        return(counter)
