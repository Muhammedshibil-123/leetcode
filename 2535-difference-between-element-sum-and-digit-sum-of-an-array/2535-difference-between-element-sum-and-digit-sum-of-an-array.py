from functools import reduce 
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total=reduce(lambda x,y: x+y ,nums,0)
        digits=[]
        for i in nums:
            s=str(i)
            if len(s)>1:
                for k in range(len(s)):
                    print(k)
                    digits.append(s[k])
            else:
                digits.append(s)
        total2=reduce(lambda x,y: x+int(y),digits,0)
        print(digits)
        print(total2)
        return total-total2
                