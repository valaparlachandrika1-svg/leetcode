class Solution(object):

    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        count = [0] * 26

        # Count characters in s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        n = len(s)

        # Try to match target from left to right
        for i in range(n):
            idx = ord(target[i]) - ord('a')

            # Use target[i] if available
            if count[idx] > 0:
                count[idx] -= 1
                continue

            # target[i] is not available.
            # Find the smallest character greater than target[i]
            for j in range(idx + 1, 26):
                if count[j] > 0:
                    # Put the smallest greater character here
                    count[j] -= 1

                    # Fill remaining positions with smallest characters
                    ans = target[:i] + chr(j + ord('a'))

                    for k in range(26):
                        ans += chr(k + ord('a')) * count[k]

                    return ans

            # No greater character is possible at this position.
            # We need to backtrack to an earlier position.
            break

        # The target itself can be formed, so find the next permutation
        # by backtracking from the end.
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Try each position from right to left
        for i in range(n - 1, -1, -1):
            # Characters before i must match target
            possible = True
            temp = count[:]

            for j in range(i):
                idx = ord(target[j]) - ord('a')
                if temp[idx] == 0:
                    possible = False
                    break
                temp[idx] -= 1

            if not possible:
                continue

            idx = ord(target[i]) - ord('a')

            # Find smallest available character greater than target[i]
            for j in range(idx + 1, 26):
                if temp[j] > 0:
                    temp[j] -= 1

                    ans = target[:i] + chr(j + ord('a'))

                    # Add remaining characters in sorted order
                    for k in range(26):
                        ans += chr(k + ord('a')) * temp[k]

                    return ans

        return ""