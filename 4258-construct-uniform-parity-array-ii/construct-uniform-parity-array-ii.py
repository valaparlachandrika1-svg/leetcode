class Solution(object):

    def uniformArray(self, nums1):

        """
        :type nums1: List[int]
        :rtype: bool
        """

        mn = min(nums1)

        # If minimum is odd, we can make every element odd
        if mn % 2 == 1:
            return True

        # Minimum is even, so every element must already be even
        for x in nums1:
            if x % 2 == 1:
                return False

        return True