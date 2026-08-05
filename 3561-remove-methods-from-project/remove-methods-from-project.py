class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)

        # Find all suspicious methods using DFS
        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if not suspicious[nei]:
                    suspicious[nei] = True
                    stack.append(nei)

        # Check if any non-suspicious method invokes a suspicious one
        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                return list(range(n))

        # Return remaining methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans