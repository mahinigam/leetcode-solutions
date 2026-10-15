class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(x: int) -> int:
            digits = list(map(int, str(x)))
            n = len(digits)

            cnt = 0
            for i in range(1, n - 1):
                peak = digits[i] > digits[i - 1] and digits[i] > digits[i + 1]
                valley = digits[i] < digits[i - 1] and digits[i] < digits[i + 1]

                if peak or valley:
                    cnt += 1
            return cnt

        ans = 0
        for x in range(num1, num2 + 1):
            ans += waviness(x)

        return ans