class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            copy=list(t)
            for i in range(len(s)):
                if s[i] not in copy:
                    return False
                else:
                    f=copy.index(s[i])
                    copy.pop(f)
                    continue 
            return True
        else:
            return False 