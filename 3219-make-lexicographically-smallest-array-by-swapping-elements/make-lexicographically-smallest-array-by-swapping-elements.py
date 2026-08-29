class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """

        n = len(nums)

        # Store (value, original_index)
        arr = sorted((nums[i], i) for i in range(n))

        i = 0

        while i < n:
            j = i

            # Find all values connected by the limit
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Indices belonging to this group
            indices = sorted(arr[k][1] for k in range(i, j + 1))

            # Values in sorted order
            values = [arr[k][0] for k in range(i, j + 1)]

            # Put smallest values at smallest indices
            for k in range(len(indices)):
                nums[indices[k]] = values[k]

            i = j + 1

        return nums