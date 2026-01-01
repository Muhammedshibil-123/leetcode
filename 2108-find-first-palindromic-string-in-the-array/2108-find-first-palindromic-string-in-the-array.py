class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            reverse=i[::-1]
            if i==reverse:
                return reverse
            else:
                pass
        return ""