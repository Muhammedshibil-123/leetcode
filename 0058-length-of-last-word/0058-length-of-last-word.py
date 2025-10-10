class Solution(object):
    def lengthOfLastWord(self, s):
        parts=s.split()
        last=parts[-1]
        return len(last)
        """
        :type s: str
        :rtype: int
        """
        