#A revised version for clarity. Still a poor man's version of a stack
class Solution:
    def isValid(self, s: str) -> bool:
        openset = {'(','{','['}
        closeset={')','}',']'}
        diction = {
            ')': '(',
            ']': '[',
            '}':'{'
        }
        basicallystack =['0']
        j = 0

        for ch in s:
            if ch in openset:
                basicallystack.append(ch)
            elif ch in closeset:
                if basicallystack[j] != diction[ch] or basicallystack == ['0']:
                    return(False)
                else:
                    basicallystack.pop(j)

            j = len(basicallystack) - 1
        if basicallystack != ['0']:
            return(False)
        return(True)
