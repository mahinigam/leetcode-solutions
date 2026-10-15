class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        FACTOR_COUNTS = {
            0: collections.Counter(),
            1: collections.Counter(),
            2: collections.Counter([2]),
            3: collections.Counter([3]),
            4: collections.Counter([2, 2]),
            5: collections.Counter([5]),
            6: collections.Counter([2, 3]),
            7: collections.Counter([7]),
            8: collections.Counter([2, 2, 2]),
            9: collections.Counter([3, 3]),
        }
        
        primeCount, ok = self._getPrimeCount(t)
        if not ok:
            return "-1"

        factorCount = self._getFactorCount(primeCount)

        if sum(factorCount.values()) > len(num):
            return "".join(d * c for d, c in factorCount.items())

        primeCountPrefix = sum(
            (FACTOR_COUNTS[int(c)] for c in num),
            start=collections.Counter(),
        )

        firstZeroIndex = next(
            (i for i, ch in enumerate(num) if ch == "0"),
            len(num),
        )

        if firstZeroIndex == len(num) and primeCount <= primeCountPrefix:
            return num

        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])

            # Remove current digit from prefix
            primeCountPrefix -= FACTOR_COUNTS[d]

            space = len(num) - 1 - i

            if i > firstZeroIndex:
                continue

            for bigger in range(d + 1, 10):
                need = self._getFactorCount(
                    primeCount
                    - primeCountPrefix
                    - FACTOR_COUNTS[bigger]
                )

                if sum(need.values()) <= space:
                    ones = space - sum(need.values())
                    return (
                        num[:i]
                        + str(bigger)
                        + "1" * ones
                        + "".join(
                            digit * cnt
                            for digit, cnt in need.items()
                        )
                    )

        factorCount = self._getFactorCount(primeCount)

        return (
            "1"
            * (len(num) + 1 - sum(factorCount.values()))
            + "".join(
                digit * cnt
                for digit, cnt in factorCount.items()
            )
        )

    def _getPrimeCount(self, t: int):
        cnt = collections.Counter()

        for p in (2, 3, 5, 7):
            while t % p == 0:
                t //= p
                cnt[p] += 1

        return cnt, t == 1

    def _getFactorCount(self, cnt):
        count8, rem2 = divmod(cnt[2], 3)
        count9, count3 = divmod(cnt[3], 2)
        count4, count2 = divmod(rem2, 2)

        count6 = 0

        if count2 == 1 and count3 == 1:
            count2 = 0
            count3 = 0
            count6 = 1

        if count3 == 1 and count4 == 1:
            count2 = 1
            count6 = 1
            count3 = 0
            count4 = 0

        return {
            "2": count2,
            "3": count3,
            "4": count4,
            "5": cnt[5],
            "6": count6,
            "7": cnt[7],
            "8": count8,
            "9": count9,
        }