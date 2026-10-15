class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        max_w = 0

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            max_w = max(max_w, w)

        def check(x):
            dist = [inf] * n
            dist[0] = 0

            indeg = indegree[:]
            q = deque(i for i in range(n) if indeg[i] == 0)

            while q:
                u = q.popleft()

                for v, w in graph[u]:
                    if w >= x and (v == n - 1 or online[v]):
                        if dist[u] != inf:
                            dist[v] = min(dist[v], dist[u] + w)

                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)

            return dist[-1] <= k

        lo, hi = 0, max_w
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo if check(lo) else -1