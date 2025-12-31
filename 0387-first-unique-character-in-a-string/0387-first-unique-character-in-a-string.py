class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Create a dictionary to count frequencies
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Step 2: Loop through the string again to find the answer
        for i, char in enumerate(s):
            if count[char] == 1:
                return i  # Found it! Return the index immediately
                
        return -1  # If we finish the loop and find nothing