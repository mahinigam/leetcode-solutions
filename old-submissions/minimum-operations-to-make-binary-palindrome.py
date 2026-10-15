class Solution:
    def isBinaryPalindrome(self, n: int) -> bool:
        b = bin(n)[2:]
        return b == b[::-1]
        
    def minOperations(self, nums: List[int]) -> List[int]:
        ans = []

        for x in nums:
            if self.isBinaryPalindrome(x):
                ans.append(0)
                continue

            d = 1
            while True:
                lower = x - d
                upper = x + d

                # lower
                if lower >= 1 and self.isBinaryPalindrome(lower):
                    ans.append(d)
                    break

                # upper
                if self.isBinaryPalindrome(upper):
                    ans.append(d)
                    break

                d += 1

        return ans