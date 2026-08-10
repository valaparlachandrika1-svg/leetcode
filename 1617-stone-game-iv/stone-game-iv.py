class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # dp[i] will store True if the player whose turn it is can force a win with i stones
        dp = [False] * (n + 1)
        
        # Pre-calculate all available perfect squares up to n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
            
        # Fill the DP table from 1 to n
        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break
                # If removing 'square' leaves the opponent in a losing position, 
                # the current player wins from position 'i'.
                if not dp[i - square]:
                    dp[i] = True
                    break
                    
        return dp[n]
        