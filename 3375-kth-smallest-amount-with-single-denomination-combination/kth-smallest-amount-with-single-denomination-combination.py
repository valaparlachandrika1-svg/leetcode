class Solution(object):

    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """

        # GCD without using math.gcd
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # LCM
        def lcm(a, b):
            return (a // gcd(a, b)) * b

        # Remove redundant coins
        coins.sort()
        useful = []

        for c in coins:
            redundant = False

            for x in useful:
                if c % x == 0:
                    redundant = True
                    break

            if not redundant:
                useful.append(c)

        coins = useful
        n = len(coins)

        # Count numbers <= x divisible by at least one coin
        def count(x):
            total = 0

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                L = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        L = lcm(L, coins[i])

                        if L > x:
                            valid = False
                            break

                if valid:
                    if bits % 2 == 1:
                        total += x // L
                    else:
                        total -= x // L

            return total

        # Binary search
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left