#a poor man's version of a stack
class Solution:
    def isValid(self, s: str) -> bool:
        openset = {'(','{','['}
        closeset={')','}',']'}
        basicallystack =['0']
        j = 0

        for ch in s:
            if ch in openset:
                basicallystack.append(ch)
            elif ch in closeset:
                if ch == ')' and basicallystack[j] != '(':
                    return(False)
                elif ch == ')' and basicallystack == ['0']:
                    return(False)
                elif ch == ')':
                    basicallystack.pop(j)
                if ch == '}' and basicallystack[j] != '{':
                    return(False)
                elif ch == '}' and basicallystack == ['0']:
                    return(False)
                elif ch == '}':
                    basicallystack.pop(j)
                if ch == ']' and basicallystack[j] != '[':
                    return(False)
                elif ch == ']' and basicallystack == ['0']:
                    return(False)
                elif ch == ']':
                    basicallystack.pop(j)
            j = len(basicallystack) - 1
            
        if basicallystack != ['0']:
            return(False)
        return(True)
