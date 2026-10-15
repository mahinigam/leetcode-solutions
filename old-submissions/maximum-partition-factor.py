class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        temp = points
        n = len(temp)
        
        if n == 2:
            return 0

        edges = []
        dists = []
        for i in range(n):
            xi, yi = temp[i]
            for j in range(i+1, n):
                xj, yj = temp[j]
                d = abs(xi-xj) + abs(yi-yj)
                edges.append((d, i, j))
                dists.append(d)

        candidates = [0] + sorted(set(dists))

        from collections import deque

        def is_bipartite_with_threshold(th):
            adj = [[] for _ in range(n)]
            for dist, i, j in edges:
                if dist < th:
                    adj[i].append(j)
                    adj[j].append(i)

            color = [-1] * n
            for start in range(n):
                if color[start] == -1:
                    color[start] = 0
                    q = deque([start])
                    while q:
                        u = q.popleft()
                        for v in adj[u]:
                            if color[v] == -1:
                                color[v] = color[u] ^ 1
                                q.append(v)
                            elif color[v] == color[u]:
                                return False

            return True

        lo, hi = 0, len(candidates) - 1
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_bipartite_with_threshold(candidates[mid]):
                ans = candidates[mid]
                lo = mid + 1
            else:
                hi = mid - 1 

        return ans