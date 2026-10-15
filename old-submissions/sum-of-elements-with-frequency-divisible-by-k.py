from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        total = 0

        for num, count in freq.items():
            if count % k == 0:
                total += num * count

        return total