class Solution(object):

    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        n = len(piles)

        # Suffix sum:
        # suffix[i] = total stones from i to n-1
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones current player can get
        # starting from index i with current M
        dp = {}

        def solve(i, M):
            if i >= n:
                return 0

            # If we can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            key = (i, M)

            if key in dp:
                return dp[key]

            best = 0

            # Try taking X piles, where 1 <= X <= 2*M
            for X in range(1, 2 * M + 1):
                # Stones opponent can get after our move
                opponent = solve(i + X, max(M, X))

                # Total remaining stones - opponent's maximum
                current = suffix[i] - opponent

                best = max(best, current)

            dp[key] = best
            return best

        return solve(0, 1)
    