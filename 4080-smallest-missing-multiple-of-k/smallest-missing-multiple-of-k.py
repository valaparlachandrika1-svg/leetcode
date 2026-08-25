class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_set = set(nums)

        multiple = k

        while multiple in num_set:
            multiple += k

        return multiple