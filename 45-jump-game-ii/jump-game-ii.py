class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):

            # Farthest index we can reach
            farthest = max(farthest, i + nums[i])

            # We have reached the end of the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest

                # Already can reach the last index
                if current_end >= n - 1:
                    break

        return jumps