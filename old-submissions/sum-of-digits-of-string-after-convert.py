class Solution:
    def getLucky(self, s: str, k: int) -> int:
        x = ''

        for ch in s:
            x += str(ord(ch) - 96)

        for _ in range(k):
            x = str(sum(int(d) for d in x))

        return int(x)