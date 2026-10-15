class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')

        # 1. Identify all blocks of contiguous '0's
        C_start = []
        C_end = []
        C_len = []
        block_id = [-1] * n

        i = 0
        b_idx = 0
        while i < n:
            if s[i] == '0':
                st = i
                while i < n and s[i] == '0':
                    block_id[i] = b_idx
                    i += 1
                en = i - 1
                C_start.append(st)
                C_end.append(en)
                C_len.append(en - st + 1)
                b_idx += 1
            else:
                i += 1

        m = b_idx

        # 2. Precompute next and previous occurrences of '0's for O(1) interval binding
        next_zero = [-1] * n
        last_seen = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                last_seen = i
            next_zero[i] = last_seen

        prev_zero = [-1] * n
        last_seen = -1
        for i in range(n):
            if s[i] == '0':
                last_seen = i
            prev_zero[i] = last_seen

        # 3. Build a Sparse Table to query the maximum sum of adjacent fully enclosed '0' blocks
        if m >= 2:
            S = [C_len[j] + C_len[j+1] for j in range(m - 1)]
            LOG = 0
            while (1 << LOG) <= len(S):
                LOG += 1
                
            st = [[0] * LOG for _ in range(len(S))]
            for i in range(len(S)):
                st[i][0] = S[i]
                
            for j in range(1, LOG):
                for i in range(len(S) - (1 << j) + 1):
                    st[i][j] = max(st[i][j-1], st[i + (1 << (j-1))][j-1])

            def query_max(L: int, R: int) -> int:
                if L > R:
                    return 0
                length = R - L + 1
                k = length.bit_length() - 1
                return max(st[L][k], st[R - (1 << k) + 1][k])
        else:
            def query_max(L: int, R: int) -> int:
                return 0

        # 4. Answer Queries
        ans = []
        for l, r in queries:
            first_0 = next_zero[l]
            last_0 = prev_zero[r]

            # If no '0' exists in the query range
            if first_0 == -1 or first_0 > r:
                ans.append(total_ones)
                continue

            a = block_id[first_0]
            b = block_id[last_0]

            # If all '0's in the query range belong to the exact same block
            if a == b:
                ans.append(total_ones)
                continue

            # If there are exactly two blocks of '0's intersecting the query
            if b == a + 1:
                z1 = C_end[a] - first_0 + 1
                z2 = last_0 - C_start[b] + 1
                gain = z1 + z2
                
            # If there are more than two blocks, check boundaries and internal adjacent sums
            else:
                z1 = C_end[a] - first_0 + 1
                z2 = C_len[a+1]
                val1 = z1 + z2

                zk_1 = C_len[b-1]
                zk = last_0 - C_start[b] + 1
                val2 = zk_1 + zk

                val3 = 0
                if b - 1 >= a + 2:
                    val3 = query_max(a + 1, b - 2)

                gain = max(val1, val2, val3)

            ans.append(total_ones + gain)

        return ans