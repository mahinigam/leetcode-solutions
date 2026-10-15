class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for num in range(low, high+1):
            s = str(num)

            if len(s) % 2:
                continue

            mid = len(s) // 2

            left = sum(int(ch) for ch in s[:mid])
            right = sum(int(ch) for ch in s[mid:])

            if left == right:
                ans += 1

        return ans