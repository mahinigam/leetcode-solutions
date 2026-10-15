class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        s = 0

        for i in str(n):
            if i != "0":
                x += i
                s += int(i)

        return int(x) * s if x else 0
