class Solution(object):

    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        # Find positions of minimum and maximum
        min_pos = nums.index(min(nums))
        max_pos = nums.index(max(nums))

        # Make min_pos the smaller index
        left = min(min_pos, max_pos)
        right = max(min_pos, max_pos)

        # 1. Remove both from the front
        front = right + 1

        # 2. Remove both from the back
        back = n - left

        # 3. Remove left from front and right from back
        both = (left + 1) + (n - right)

        return min(front, back, both)