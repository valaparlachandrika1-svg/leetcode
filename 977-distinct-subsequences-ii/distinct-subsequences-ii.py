class Solution(object):

    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        
        dp = 1  # includes the empty subsequence
        last = [0] * 26
        
        for ch in s:
            i = ord(ch) - ord('a')
            
            new_dp = (2 * dp - last[i]) % MOD
            last[i] = dp
            dp = new_dp
        
        # Remove the empty subsequence
        return (dp - 1) % MOD