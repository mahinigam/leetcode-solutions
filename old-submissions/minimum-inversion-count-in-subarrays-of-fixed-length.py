class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size+1)

    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)

        sorted_unique = sorted(set(nums))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        ranks = [rank_map[x] for x in nums]
        max_rank = len(sorted_unique)

        bit = FenwickTree(max_rank)
        current_inversions = 0

        for i in range(k):
            rank = ranks[i]
            count_larger = i - bit.query(rank)
            current_inversions += count_larger
            bit.update(rank, 1)

        min_inv = current_inversions

        for i in range(k, n):
            out_rank = ranks[i-k]

            smaller_count = bit.query(out_rank - 1)
            current_inversions -= smaller_count

            bit.update(out_rank, -1)

            in_rank = ranks[i]

            larger_count = (k - 1) - bit.query(in_rank)
            current_inversions += larger_count

            bit.update(in_rank, 1)

            if current_inversions < min_inv:
                min_inv = current_inversions

        return min_inv