
class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        start = 1000
        
        while start <= n:
            ans += (n - start + 1)
            start *= 1000
            
        return ans