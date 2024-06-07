class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(' ')
        dictionary = sorted(dictionary, key = len)


        for i in range(len(dictionary)):
            for j in range(len(sentence)):
                count = 0
                if len(dictionary[i]) < len(sentence[j]):
                    for l in range(len(dictionary[i])):
                        if dictionary[i][l] == sentence[j][l]:
                            count +=1
                        if count == len(dictionary[i]):
                            sentence[j] = dictionary[i]

        final = ''

        for k in range(len(sentence)):
            final+= sentence[k]
            if k != (len(sentence) - 1):
                final += ' '

        return(final)
        
