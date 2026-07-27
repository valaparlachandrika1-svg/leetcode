class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        second = 0

        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num

        return (first - 1) * (second - 1)