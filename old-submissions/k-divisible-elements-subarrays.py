class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        seen = set()
        n = len(nums)

        for i in range(n):
            cnt = 0
            cur = []

            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt += 1
                if cnt > k:
                    break

                cur.append(nums[j])
                seen.add(tuple(cur))

        return len(seen)