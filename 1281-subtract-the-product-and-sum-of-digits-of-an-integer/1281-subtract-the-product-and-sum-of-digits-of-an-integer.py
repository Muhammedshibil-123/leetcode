from functools import reduce
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=list(map(int,str(n)))
        Pdigits=reduce(lambda acc,item:acc*item,n,1)
        SumDigits=reduce(lambda acc,item:acc+item,n,0)
        return Pdigits-SumDigits
        