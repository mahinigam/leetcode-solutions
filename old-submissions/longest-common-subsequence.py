class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[-1] * m for _ in range(n)]

        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + helper(i+1, j+1)
                return dp[i][j]

            else:
                dp[i][j] = max(helper(i+1, j), helper(i, j+1))
                return dp[i][j]

        return helper(0, 0)