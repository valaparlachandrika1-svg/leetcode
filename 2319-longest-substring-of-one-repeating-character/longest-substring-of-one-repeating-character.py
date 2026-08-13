class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """

        n = len(s)
        tree = [None] * (4 * n)

        # Each node stores:
        # [left_char, right_char, prefix, suffix, maximum, length]

        def merge(a, b):
            left_char = a[0]
            right_char = b[1]

            prefix = a[2]
            suffix = b[3]

            maximum = max(a[4], b[4])

            # If the entire left segment has the same character
            # and it matches the first character of right segment
            if a[2] == a[5] and a[1] == b[0]:
                prefix = a[5] + b[2]

            # If the entire right segment has the same character
            # and it matches the last character of left segment
            if b[3] == b[5] and a[1] == b[0]:
                suffix = a[3] + b[5]

            # If characters at the boundary are equal,
            # combine left suffix and right prefix
            if a[1] == b[0]:
                maximum = max(maximum, a[3] + b[2])

            length = a[5] + b[5]

            return [
                left_char,
                right_char,
                prefix,
                suffix,
                maximum,
                length
            ]

        def build(node, left, right):
            if left == right:
                ch = s[left]
                tree[node] = [ch, ch, 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index, ch):
            if left == right:
                tree[node] = [ch, ch, 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, ch)
            else:
                update(node * 2 + 1, mid + 1, right, index, ch)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # Build tree
        build(1, 0, n - 1)

        result = []

        # Process queries
        for i in range(len(queryCharacters)):
            index = queryIndices[i]
            ch = queryCharacters[i]

            update(1, 0, n - 1, index, ch)

            result.append(tree[1][4])

        return result