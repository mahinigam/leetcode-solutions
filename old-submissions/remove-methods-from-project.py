class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        rev = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)
            rev[v].append(u)

        suspicious = [False] * n

        def dfs(u):
            suspicious[u] = True
            for v in graph[u]:
                if not suspicious[v]:
                    dfs(v)

        # Find all suspicious methods
        dfs(k)

        # If any suspicious method is called by a non-suspicious method,
        # we cannot remove anything.
        for v in range(n):
            if not suspicious[v]:
                continue
            for u in rev[v]:
                if not suspicious[u]:
                    return list(range(n))

        # Return remaining methods
        return [i for i in range(n) if not suspicious[i]]