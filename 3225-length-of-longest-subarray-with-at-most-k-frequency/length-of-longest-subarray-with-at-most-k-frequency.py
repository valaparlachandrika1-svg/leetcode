class Solution(object):

    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        freq = {}
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # Add current element
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # If frequency exceeds k, move left
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length