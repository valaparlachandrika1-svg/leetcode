class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)
        
        # right0[j]: max index in word1 to match word2[j:] with 0 changes
        right0 = [-1] * (m + 1)
        right0[m] = n
        
        ptr0 = n - 1
        for j in range(m - 1, -1, -1):
            limit = right0[j + 1] - 1
            ptr0 = min(ptr0, limit)
            while ptr0 >= 0 and word1[ptr0] != word2[j]:
                ptr0 -= 1
            right0[j] = ptr0

        # right1[j]: max index in word1 to match word2[j:] with AT MOST 1 change
        right1 = [-1] * (m + 1)
        right1[m] = n
        
        for j in range(m - 1, -1, -1):
            # Option 1: Use 1 change at word2[j]
            opt1 = right0[j + 1] - 1
            
            # Option 2: Match word2[j] exactly at or before right1[j + 1] - 1
            opt2 = -1
            limit = right1[j + 1] - 1
            # Search leftwards starting from limit for exact match
            p = min(n - 1, limit)
            while p >= 0 and word1[p] != word2[j]:
                p -= 1
            opt2 = p
            
            right1[j] = max(opt1, opt2)

        result = []
        changed = False
        j = 0
        
        # Greedily match from left to right for lexicographically smallest sequence
        for i in range(n):
            if j == m:
                break
                
            if word1[i] == word2[j]:
                # Exact match
                max_allowed = right0[j + 1] if changed else right1[j + 1]
                if i < max_allowed:
                    result.append(i)
                    j += 1
            else:
                # Mismatch: use 1 change if not already used
                if not changed and i < right0[j + 1]:
                    result.append(i)
                    changed = True
                    j += 1

        return result if len(result) == m else []