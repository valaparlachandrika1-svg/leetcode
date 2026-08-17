from bisect import bisect_left

class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        if n <= 1:
            return 0
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = prefix[j + 1] - prefix[i]
                
                # Binary search to find the first index k where left_sum >= right_sum
                # Target: prefix[k+1] - prefix[i] >= total / 2.0
                target = prefix[i] + total / 2.0
                
                # bisect_left gives index in prefix array
                mid_idx = bisect_left(prefix, target, i + 1, j + 1) - 1
                
                res = 0
                
                # k in [i, mid_idx - 1]: strictly left_sum < right_sum
                if mid_idx - 1 >= i:
                    res = max(res, max_left[i][mid_idx - 1])
                
                # k in [mid_idx + 1, j - 1]: strictly left_sum > right_sum
                if mid_idx + 1 < j:
                    res = max(res, max_right[mid_idx + 1][j])
                
                # Check k = mid_idx
                if mid_idx < j:
                    left_sum = prefix[mid_idx + 1] - prefix[i]
                    right_sum = total - left_sum
                    
                    if left_sum == right_sum:
                        res = max(res, max_left[i][mid_idx])
                        res = max(res, max_right[mid_idx + 1][j])
                    elif left_sum < right_sum:
                        res = max(res, left_sum + dp[i][mid_idx])
                    else:
                        res = max(res, right_sum + dp[mid_idx + 1][j])
                
                dp[i][j] = res
                max_left[i][j] = max(max_left[i][j - 1], res + total)
                max_right[i][j] = max(max_right[i + 1][j], res + total)
                
        return dp[0][n - 1]