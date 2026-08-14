class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []
        candidates.sort()

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break

                path.append(candidates[i])

                # i is passed again because the same number
                # can be used unlimited times
                backtrack(i, target - candidates[i], path)

                path.pop()

        backtrack(0, target, [])
        return result