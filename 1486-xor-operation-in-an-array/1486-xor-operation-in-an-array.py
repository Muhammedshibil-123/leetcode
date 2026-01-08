class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        flist=[]
        for i in range(start,start+n):
            if i==start:
                flist.append(i)
            else:
                flist.append(flist[-1]+2)
            print(flist)
        result=0
        for i in flist:
            result=result^i
            print(result)
            
        return result