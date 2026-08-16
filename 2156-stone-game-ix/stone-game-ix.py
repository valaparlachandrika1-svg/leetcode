class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        # Stones divisible by 3
        # do not change the remainder.
        if count[0] % 2 == 0:
            return count[1] > 0 and count[2] > 0

        # Odd number of 0-mod-3 stones
        return abs(count[1] - count[2]) > 2       