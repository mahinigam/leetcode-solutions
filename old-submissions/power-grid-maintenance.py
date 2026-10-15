import heapq
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pb] < self.rank[pa]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1


class Solution:
    def processQueries(self, n: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(n)

        # Build connected components
        for u, v in connections:
            dsu.union(u, v)

        # Each component -> min-heap of station IDs
        comp_heap = {}
        for i in range(1, n + 1):
            root = dsu.find(i)
            if root not in comp_heap:
                comp_heap[root] = []
            comp_heap[root].append(i)

        # Convert to heap
        for h in comp_heap.values():
            heapq.heapify(h)

        online = [True] * (n + 1)
        res = []

        for typ, x in queries:
            if typ == 2:
                # Take station offline
                online[x] = False
            else:
                # Query
                if online[x]:
                    res.append(x)
                else:
                    root = dsu.find(x)
                    heap = comp_heap[root]

                    # Lazy removal of offline nodes
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)

                    if not heap:
                        res.append(-1)
                    else:
                        res.append(heap[0])

        return res