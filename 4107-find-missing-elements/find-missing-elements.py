class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        low = min(nums)
        high = max(nums)

        s = set(nums)
        ans = []

        for i in range(low, high + 1):
            if i not in s:
                ans.append(i)

        return ans