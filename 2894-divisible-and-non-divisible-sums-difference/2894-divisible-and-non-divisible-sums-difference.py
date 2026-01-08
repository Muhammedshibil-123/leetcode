class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        non=[]
        divisble=[]
        for i in range(1,n+1):
            if i%m==0:
                divisble.append(i)
            else:
                non.append(i)
        
        return sum(non)-sum(divisble)
                
        