class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}

        def dfs(left, right):
            if left == right:
                return nums[left]

            if (left, right) in memo:
                return memo[(left, right)]

            pick_left = nums[left] - dfs(left + 1, right)
            pick_right = nums[right] - dfs(left, right - 1)

            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]

        return dfs(0, len(nums) - 1) >= 0