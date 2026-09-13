class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """

        count = 0

        # Count how many times each digit appears
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        # Check all 3-digit even numbers
        for num in range(100, 1000, 2):

            # Get the three digits
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Make a temporary frequency array
            used = [0] * 10
            used[a] += 1
            used[b] += 1
            used[c] += 1

            # Check whether we have enough copies
            possible = True

            for d in range(10):
                if used[d] > freq[d]:
                    possible = False
                    break

            if possible:
                count += 1

        return count