class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        left = []
        middle = ""

        for i in range(26):
            left.append(chr(i + ord('a')) * (freq[i] // 2))
            if freq[i] % 2 == 1:
                middle = chr(i + ord('a'))

        left = "".join(left)
        return left + middle + left[::-1]
        