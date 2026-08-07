class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        # Step 1: Factorize t into prime factors 2, 3, 5, 7
        temp = t
        counts = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while temp % p == 0:
                counts[p] += 1
                temp //= p
        
        # If t has prime factors greater than 7, no zero-free digit product can be divisible by t
        if temp > 1:
            return "-1"

        # Step 2: Bottom-Up Iterative DP for factors 2 and 3
        # Max required counts for 2 and 3 when t <= 10^14 is around 47 and 30
        max_r2 = counts[2] + 1
        max_r3 = counts[3] + 1

        # dp[r2][r3] stores the optimal string for (r2, r3)
        dp = [[None] * max_r3 for _ in range(max_r2)]
        dp[0][0] = ""

        digits_info = [
            (9, 0, 2), (8, 3, 0), (6, 1, 1),
            (4, 2, 0), (3, 0, 1), (2, 1, 0)
        ]

        for r2 in range(max_r2):
            for r3 in range(max_r3):
                if r2 == 0 and r3 == 0:
                    continue
                best = None
                for d, p2, p3 in digits_info:
                    prev_2 = max(0, r2 - p2)
                    prev_3 = max(0, r3 - p3)
                    prev_str = dp[prev_2][prev_3]
                    if prev_str is not None:
                        cand = "".join(sorted(str(d) + prev_str))
                        if best is None or (len(cand), cand) < (len(best), best):
                            best = cand
                dp[r2][r3] = best

        def get_best_23(r2, r3):
            r2 = max(0, min(r2, counts[2]))
            r3 = max(0, min(r3, counts[3]))
            return dp[r2][r3]

        def get_min_suffix(r2, r3, r5, r7, avail_len):
            """Returns lexicographically smallest suffix of length `avail_len`."""
            r5 = max(0, r5)
            r7 = max(0, r7)
            needed_23 = get_best_23(r2, r3)
            needed_all = "5" * r5 + "7" * r7 + needed_23
            if len(needed_all) > avail_len:
                return None
            
            ones = "1" * (avail_len - len(needed_all))
            return ones + "".join(sorted(needed_all))

        n = len(num)

        # Step 3: Check for zero in num and compute prefix factors
        digit_p = {
            '1': (0, 0, 0, 0), '2': (1, 0, 0, 0), '3': (0, 1, 0, 0),
            '4': (2, 0, 0, 0), '5': (0, 0, 1, 0), '6': (1, 1, 0, 0),
            '7': (0, 0, 0, 1), '8': (3, 0, 0, 0), '9': (0, 2, 0, 0)
        }

        pref_factors = [(0, 0, 0, 0)] * (n + 1)
        first_zero_idx = -1
        for i, ch in enumerate(num):
            if ch == '0':
                first_zero_idx = i
                break
            p2, p3, p5, p7 = digit_p[ch]
            prev_2, prev_3, prev_5, prev_7 = pref_factors[i]
            pref_factors[i + 1] = (prev_2 + p2, prev_3 + p3, prev_5 + p5, prev_7 + p7)

        max_prefix = first_zero_idx if first_zero_idx != -1 else n

        # Step 4: Try prefix matching of length n
        for i in range(max_prefix, -1, -1):
            cur_2, cur_3, cur_5, cur_7 = pref_factors[i]
            
            # Start digit for index i
            start_d = 1 if i == n else int(num[i]) + (0 if i == max_prefix and first_zero_idx == -1 else 1)

            for d in range(start_d, 10):
                d_ch = str(d)
                dp2, dp3, dp5, dp7 = digit_p[d_ch]
                
                rem_2 = counts[2] - (cur_2 + dp2 if i < n else cur_2)
                rem_3 = counts[3] - (cur_3 + dp3 if i < n else cur_3)
                rem_5 = counts[5] - (cur_5 + dp5 if i < n else cur_5)
                rem_7 = counts[7] - (cur_7 + dp7 if i < n else cur_7)

                avail = n - (i + 1) if i < n else 0
                suffix = get_min_suffix(rem_2, rem_3, rem_5, rem_7, avail)
                
                if suffix is not None:
                    prefix = num[:i] + (d_ch if i < n else "")
                    return prefix + suffix

        # Step 5: If no solution of length `n`, construct minimal solution longer than `n`
        needed_23 = get_best_23(counts[2], counts[3])
        needed_len = len(needed_23) + counts[5] + counts[7]
        target_len = max(n + 1, needed_len)

        return get_min_suffix(counts[2], counts[3], counts[5], counts[7], target_len)