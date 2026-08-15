class Solution(object):

    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        xor = 0
        has_non_zero = False
        
        for num in nums:
            xor ^= num
            if num != 0:
                has_non_zero = True
        
        # XOR of all elements is non-zero
        if xor != 0:
            return len(nums)
        
        # XOR is zero and all elements are zero
        if not has_non_zero:
            return 0
        
        # XOR is zero, but at least one element is non-zero
        return len(nums) - 1