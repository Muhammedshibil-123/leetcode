class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sumdecimal=int(a,2)+int(b,2)
        result=bin(sumdecimal)[2:]
        return result