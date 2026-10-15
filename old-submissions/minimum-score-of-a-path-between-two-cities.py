class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, distance in roads:
            graph[u].append((v, distance))
            graph[v].append((u, distance))

        visited = [False] * (n + 1)
        stack = [1]
        visited[1] = True

        answer = float("inf")

        while stack:
            city = stack.pop()

            for neighbor, distance in graph[city]:
                answer = min(answer, distance)

                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        return answer