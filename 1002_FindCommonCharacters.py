class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        for i in range(len(words)):
            words[i] = list(words[i])
        
        copy = words
        letters = []

        for j in range(len(words[0])):
            k=1
            counter = 1
            while k < len(words):
                if words[0][j] in copy[k]:
                    del copy[k][copy[k].index(words[0][j])]
                    counter +=1
                k+=1
            if counter >= len(words):
                letters.append(words[0][j])
        return(letters)
