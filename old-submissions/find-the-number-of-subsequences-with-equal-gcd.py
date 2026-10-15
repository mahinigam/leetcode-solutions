class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        @cache
        def dfs(i: int, g1: int, g2: int) -> int:
            if i == n:
                return int(g1 > 0 and g1 == g2)

            x = nums[i]

            # Skip nums[i]
            ans = dfs(i + 1, g1, g2)

            # Put nums[i] into seq1
            ng1 = x if g1 == 0 else gcd(g1, x)
            ans += dfs(i + 1, ng1, g2)

            # Put nums[i] into seq2
            ng2 = x if g2 == 0 else gcd(g2, x)
            ans += dfs(i + 1, g1, ng2)

            return ans % MOD

        return dfs(0, 0, 0)