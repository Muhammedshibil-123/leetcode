class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        print(count)
        result=0
        resultOg=0
        for i,k in count.items():
            print(k)
            if k>result:
                result=k
                resultOg=i
            else:
                continue
        return resultOg