class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        total_ones = s.count('1')
        
        # 1. Extract contiguous '0' blocks [start, end]
        zero_groups = []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                zero_groups.append((start, i - 1))
            else:
                i += 1
                
        num_groups = len(zero_groups)
        
        # 2. Precompute O(1) lookups for first and last overlapping '0' groups
        first_group = [num_groups] * n
        last_group = [-1] * n
        
        g_ptr = 0
        for idx in range(n):
            while g_ptr < num_groups and zero_groups[g_ptr][1] < idx:
                g_ptr += 1
            first_group[idx] = g_ptr
            
        g_ptr = 0
        for idx in range(n):
            while g_ptr < num_groups and zero_groups[g_ptr][0] <= idx:
                g_ptr += 1
            last_group[idx] = g_ptr - 1
            
        # 3. Build Sparse Table over sum of lengths of adjacent '0' blocks
        if num_groups >= 2:
            m = num_groups - 1
            log_m = m.bit_length()
            st = [[0] * m for _ in range(log_m)]
            st[0] = [
                (zero_groups[j][1] - zero_groups[j][0] + 1) + 
                (zero_groups[j + 1][1] - zero_groups[j + 1][0] + 1)
                for j in range(m)
            ]
            for i_level in range(1, log_m):
                length = 1 << (i_level - 1)
                for j in range(m - (1 << i_level) + 1):
                    st[i_level][j] = max(st[i_level - 1][j], st[i_level - 1][j + length])
                    
            def query_st(ql, qr):
                if ql > qr:
                    return 0
                k = (qr - ql + 1).bit_length() - 1
                return max(st[k][ql], st[k][qr - (1 << k) + 1])
        else:
            def query_st(ql, qr):
                return 0

        # Helper to compute clipped length of group g_idx inside [l, r]
        def get_len(g_idx, l, r):
            S, E = zero_groups[g_idx]
            return max(0, min(E, r) - max(S, l) + 1)

        # 4. Process each query in O(1) time
        ans = []
        for l, r in queries:
            first = first_group[l]
            last = last_group[r]
            
            if first >= last:
                ans.append(total_ones)
                continue
            
            max_gain = 0
            
            # Check boundary pair starting at 'first'
            gain1 = get_len(first, l, r) + get_len(first + 1, l, r)
            if gain1 > max_gain:
                max_gain = gain1
                
            # Check boundary pair ending at 'last'
            gain2 = get_len(last - 1, l, r) + get_len(last, l, r)
            if gain2 > max_gain:
                max_gain = gain2
                
            # Check fully internal adjacent pairs via Sparse Table
            if first + 1 <= last - 2:
                st_gain = query_st(first + 1, last - 2)
                if st_gain > max_gain:
                    max_gain = st_gain
                    
            ans.append(total_ones + max_gain)
            
        return ans