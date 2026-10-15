class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = Counter(nums)

        exact_pairs = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            cnt = 0
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]
                exact_pairs[g] -= exact_pairs[multiple]
            exact_pairs[g] += cnt * (cnt - 1) // 2

        prefix = list(accumulate(exact_pairs))

        return [bisect_right(prefix, q) for q in queries]