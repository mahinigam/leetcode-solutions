class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def solve(i, current_amount):
            if current_amount == 0:
                return 0
            if current_amount < 0 or i == len(coins):
                return float('inf')

            if (i, current_amount) in dp:
                return dp[(i, current_amount)]

            take = 1 + solve(i, current_amount - coins[i])

            not_take = solve(i + 1, current_amount)

            dp[(i, current_amount)] = min(take, not_take)
            return dp[(i, current_amount)]

        result = solve(0, amount)
        return result if result != float('inf') else -1