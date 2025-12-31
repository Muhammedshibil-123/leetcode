class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        removed=set(sentence)
        if len(removed)<=25:
            return False
        for i in removed:
            if ord(i)>=97 and ord(i) <=122:
                pass
            else:
                return False
        
        return True