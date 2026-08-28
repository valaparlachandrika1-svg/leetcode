class Solution(object):

    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        from collections import Counter

        n = len(s)
        count = Counter(s)

        # Check whether a palindrome can be formed
        odd = 0
        middle = ""

        for ch in count:
            if count[ch] % 2 == 1:
                odd += 1
                middle = ch

        if odd > 1:
            return ""

        # Number of characters in left half
        half_len = n // 2

        # Character counts for left half
        half_count = [0] * 26

        for ch in count:
            half_count[ord(ch) - ord('a')] = count[ch] // 2

        def build(left):
            if n % 2 == 0:
                return left + left[::-1]
            else:
                return left + middle + left[::-1]

        # --------------------------------------------------
        # STEP 1:
        # Check if target's first half itself can be used.
        # This is important because the complete palindrome
        # may be greater than target even when the left halves
        # are equal.
        # --------------------------------------------------

        target_half = target[:half_len]

        available = half_count[:]
        possible = True

        for ch in target_half:
            idx = ord(ch) - ord('a')

            if available[idx] == 0:
                possible = False
                break

            available[idx] -= 1

        if possible:
            candidate = build(target_half)

            if candidate > target:
                return candidate

        # --------------------------------------------------
        # STEP 2:
        # Find the smallest left half strictly greater than
        # target_half.
        # --------------------------------------------------

        for i in range(half_len - 1, -1, -1):

            available = half_count[:]

            # Match target prefix before position i
            possible = True

            for j in range(i):
                idx = ord(target_half[j]) - ord('a')

                if available[idx] == 0:
                    possible = False
                    break

                available[idx] -= 1

            if not possible:
                continue

            # Find smallest character greater than target[i]
            current = ord(target_half[i]) - ord('a')
            chosen = -1

            for c in range(current + 1, 26):
                if available[c] > 0:
                    chosen = c
                    break

            if chosen == -1:
                continue

            # Construct left half
            left = target_half[:i]
            left += chr(chosen + ord('a'))

            available[chosen] -= 1

            # Add remaining characters in sorted order
            for c in range(26):
                if available[c] > 0:
                    left += chr(c + ord('a')) * available[c]

            candidate = build(left)

            if candidate > target:
                return candidate

        return ""