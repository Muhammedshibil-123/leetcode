from functools import reduce
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result=0
        for i in accounts:
            wealth=reduce(lambda acc,item:acc+item,i,0)
            if wealth > result:
                result=wealth
        
        return result
