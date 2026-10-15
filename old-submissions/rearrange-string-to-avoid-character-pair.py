class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        cnt_x, cnt_y = 0, 0
        other = []

        for ch in s:
            if ch == x:
                cnt_x += 1
            elif ch == y:
                cnt_y += 1
            else:
                other.append(ch)

        return y * cnt_y + "".join(other) + x * cnt_x