class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        @cache
        def dp(i, M):
            if i == n:
                return 0

            ans = 0

            # Take X piles, where 1 <= X <= 2*M
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break

                ans = max(
                    ans,
                    suffix[i] - dp(i + X, max(M, X))
                )

            return ans

        return dp(0, 1)