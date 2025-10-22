class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numbers=nums1+nums2
        numbers.sort()
        mid=len(numbers)//2
        if len(numbers) %2 == 0 :
            median=(numbers[mid-1]+numbers[mid])/2
            return median
        else :
            median=numbers[mid]  
            return median           
