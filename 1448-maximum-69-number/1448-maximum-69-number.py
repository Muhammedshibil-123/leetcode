class Solution:
    def maximum69Number (self, num: int) -> int:
        num1=str(num)
        result=[]
        for i in range(len(num1)):
            if num1[i] == 9:
                ans=num1[:i] + '6' + num1[i+1:]
                result.append(ans)
            else:
                ans=num1[:i] + '9' + num1[i+1:]
                result.append(ans)
        
        result.sort()
        return int(result[len(result)-1])

                
         