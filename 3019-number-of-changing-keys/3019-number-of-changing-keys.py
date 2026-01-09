class Solution:
    def countKeyChanges(self, s: str) -> int:
        cap=s.upper()
        print(cap)
        result=0
        for i in range(len(cap)-1):
            if not cap[i]==cap[i+1]:
                result+=1
                 
            
        return result
                

                
         
        