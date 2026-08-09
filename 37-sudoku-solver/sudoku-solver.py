class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Pre-populate sets to track used digits in O(1) time
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)

        def backtrack(index):
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)

            for digit in map(str, range(1, 10)):
                if (
                    digit not in rows[r]
                    and digit not in cols[c]
                    and digit not in boxes[box_idx]
                ):
                    # Place digit
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)

                    if backtrack(index + 1):
                        return True

                    # Backtrack (remove digit)
                    board[r][c] = "."
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)

            return False

        backtrack(0)
        