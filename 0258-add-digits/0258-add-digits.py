class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)            
        
        while len(num) > 1:         
            result = 0              
            
            for i in range(len(num)):
                result += int(num[i])   
            
            num = str(result)       
        
        return int(num)          
