class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        n = len(nums1)

        # If all numbers are even, keep them as they are
        all_even = True
        for x in nums1:
            if x % 2 != 0:
                all_even = False
                break

        if all_even:
            return True

        # If there is at least one odd number,
        # use that odd number to make every even number odd.
        has_odd = False
        for x in nums1:
            if x % 2 != 0:
                has_odd = True
                break

        return has_odd