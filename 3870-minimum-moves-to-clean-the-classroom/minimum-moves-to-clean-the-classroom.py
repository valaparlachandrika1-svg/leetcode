class Solution(object):

    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        from collections import deque

        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter = []

        # Find start and litter
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        k = len(litter)

        if k == 0:
            return 0

        # Assign a bit to every litter
        litter_id = {}
        for i in range(k):
            litter_id[litter[i]] = i

        full_mask = (1 << k) - 1

        # BFS state:
        # (row, col, remaining_energy, mask)
        q = deque()
        q.append((start[0], start[1], energy, 0))

        # best[r][c][mask] = maximum energy with which
        # we have reached (r,c) having collected mask.
        #
        # Use a dictionary to avoid allocating a huge 3D array.
        best = {}
        best[(start[0], start[1], 0)] = energy

        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

        steps = 0

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == full_mask:
                    return steps

                for dr, dc in moves:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # Need 1 energy for the move
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    cell = classroom[nr][nc]

                    # Collect litter
                    if cell == 'L':
                        bit = litter_id[(nr, nc)]
                        nmask |= (1 << bit)

                    # Reset energy
                    if cell == 'R':
                        ne = energy

                    key = (nr, nc, nmask)

                    # If we have already reached this position
                    # with the same litter collected and MORE energy,
                    # this state is useless.
                    if key in best and best[key] >= ne:
                        continue

                    best[key] = ne
                    q.append((nr, nc, ne, nmask))

            steps += 1

        return -1