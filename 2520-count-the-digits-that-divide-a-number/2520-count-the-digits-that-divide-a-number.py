class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        num1=list(map(int,str(num)))
        for i in num1:
            if num%i==0:
                count+=1
            else:
                pass
        return count

