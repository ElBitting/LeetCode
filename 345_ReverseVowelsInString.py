class Solution:
    def reverseVowels(self, s: str) -> str:
        j =0
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        vowel_locations = []
        while j < len(s):
            if s[j] in vowels:
                vowel_locations.append(j)
            j +=1
        
        d = len(vowel_locations)
        b = 0
        c = 0
        f = 0

        solute = list(s)
        
        while b < d:
            d -=1
            c = vowel_locations[b]
            f = vowel_locations[d]
            solute[f] = s[c]
            solute[c] = s[f]
            b += 1
        solution = ''.join(solute)
        return(solution)
