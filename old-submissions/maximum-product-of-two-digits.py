class Solution:
    def maxProduct(self, n: int) -> int:
        # arr = [int(x) for x in list(str(n))]

        # arr.sort()

        # return arr[-1] * arr[-2]

        first = second = 0

        for d in map(int, str(n)):
            if d >= first:
                second = first
                first = d
            elif d > second:
                second = d

        return first * second