class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        double=0
        single=0
        for i in nums:
            if len(str(i))>=2:
                double+=i
            else:
                single+=i
        if double == single:
            return False
        else:
            return True
                