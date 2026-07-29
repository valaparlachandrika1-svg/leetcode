class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        from collections import Counter

        freq = Counter(s)

        half = {}
        mid = ""
        total = 0

        for ch in sorted(freq):
            half[ch] = freq[ch] // 2
            total += half[ch]
            if freq[ch] % 2:
                mid = ch

        LIMIT = k

        def count_perms(cnt, rem):
            res = 1
            left = rem
            for v in cnt.values():
                if v == 0:
                    continue
                r = min(v, left - v)
                ways = 1
                for i in range(1, r + 1):
                    ways = ways * (left - r + i) // i
                    if ways > LIMIT:
                        ways = LIMIT + 1
                        break
                res *= ways
                if res > LIMIT:
                    return LIMIT + 1
                left -= v
            return res

        if count_perms(half, total) < k:
            return ""

        first = []

        while total > 0:
            for ch in sorted(half.keys()):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                ways = count_perms(half, total - 1)

                if ways >= k:
                    first.append(ch)
                    total -= 1
                    break
                else:
                    k -= ways
                    half[ch] += 1

        first = "".join(first)
        return first + mid + first[::-1]
        