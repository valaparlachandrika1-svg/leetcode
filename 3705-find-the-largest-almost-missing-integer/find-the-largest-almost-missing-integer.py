class Solution(object):

    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = {}

        # Check every subarray of size k
        for i in range(len(nums) - k + 1):
            # Set avoids counting the same number twice
            # within one subarray
            seen = set(nums[i:i + k])

            for x in seen:
                count[x] = count.get(x, 0) + 1

        # Find the largest number appearing in exactly one subarray
        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans