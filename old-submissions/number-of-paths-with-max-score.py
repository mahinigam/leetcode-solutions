class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        # E is at (0, 0)
        score[0][0] = 0
        ways[0][0] = 1

        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X' or (i == 0 and j == 0):
                    continue

                best = -1
                count = 0

                for di, dj in [(-1, 0), (0, -1), (-1, -1)]:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < n and 0 <= nj < n and score[ni][nj] != -1:
                        if score[ni][nj] > best:
                            best = score[ni][nj]
                            count = ways[ni][nj]
                        elif score[ni][nj] == best:
                            count = (count + ways[ni][nj]) % MOD

                # Cell is unreachable
                if best == -1:
                    continue

                value = 0 if board[i][j] == 'S' else int(board[i][j])

                score[i][j] = best + value
                ways[i][j] = count

        if score[n - 1][n - 1] == -1:
            return [0, 0]

        return [
            score[n - 1][n - 1],
            ways[n - 1][n - 1] % MOD
        ]