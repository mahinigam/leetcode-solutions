class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10 ** 9 + 7

        c1, c2 = 0, 0
        swaps = 0

        for num in nums:
            if num < a:
                swaps = (swaps + c1 + c2) % MOD
            elif a <= num <= b:
                swaps = (swaps + c2) % MOD
                c1 += 1
            else:
                c2 += 1

        return swaps