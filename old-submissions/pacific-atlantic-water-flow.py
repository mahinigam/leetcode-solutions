class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev_height):
            if ((r, c) in visited or 
                r < 0 or r >= m or 
                c < 0 or c >= n or 
                heights[r][c] < prev_height):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # DFS from Pacific border (top row + left column)
        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
        for c in range(n):
            dfs(0, c, pacific, heights[0][c])

        # DFS from Atlantic border (bottom row + right column)
        for r in range(m):
            dfs(r, n - 1, atlantic, heights[r][n - 1])
        for c in range(n):
            dfs(m - 1, c, atlantic, heights[m - 1][c])

        # Intersection: cells reachable by both oceans
        return list(map(list, pacific & atlantic))
