class Solution(object):

    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """

        # Store reserved seats for each row
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # Initially, every row can fit 2 groups
        # (seats 2-5 and 6-9)
        result = 2 * n

        for row, seats in rows.items():

            # If seats 2,3,4,5 are free
            left = all(seat not in seats for seat in [2, 3, 4, 5])

            # If seats 4,5,6,7 are free
            middle = all(seat not in seats for seat in [4, 5, 6, 7])

            # If seats 6,7,8,9 are free
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            # Determine how many groups this row can accommodate
            if left and right:
                # Two groups: 2-5 and 6-9
                groups = 2

            elif left or middle or right:
                # Only one of the blocks can be used
                groups = 1

            else:
                groups = 0

            # This row was counted as 2 initially,
            # so replace its contribution
            result -= 2
            result += groups

        return result