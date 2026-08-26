class Solution(object):

    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        n = len(s)
        left = 0
        ones = 0
        best = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            # Keep shrinking while we have at least k ones
            while ones >= k:
                if ones == k:
                    current = s[left:right + 1]

                    # Update if shorter or same length but lexicographically smaller
                    if best == "" or len(current) < len(best) or \
                       (len(current) == len(best) and current < best):
                        best = current

                if s[left] == '1':
                    ones -= 1
                left += 1

        return best