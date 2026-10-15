import collections

class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        temp = (n, edges, nums)

        MAX_NUM = 100001
        sf_map = list(range(MAX_NUM))
        i = 2
        while i*i < MAX_NUM:
            square = i*i
            for j in range(square, MAX_NUM, square):
                while sf_map[j] % square == 0:
                    sf_map[j] //= square
            i += 1

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        sf_nums = [sf_map[num] for num in nums]

        self.total_sum = 0
        path_counts = collections.defaultdict(int)

        def dfs(u: int, p: int):
            my_sf = sf_nums[u]
            self.total_sum += path_counts.get(my_sf, 0)
            path_counts[my_sf] += 1

            for v in adj.get(u, []):
                if v != p:
                    dfs(v, u)

            path_counts[my_sf] -= 1

        dfs(0, -1)

        return self.total_sum
        