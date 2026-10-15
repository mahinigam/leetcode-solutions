class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def build(starts, durations):
            rides = sorted(zip(starts, durations))
            starts = [s for s, _ in rides]
            n = len(rides)

            pref = [0] * n
            pref[0] = rides[0][1]

            for i in range(1, n):
                pref[i] = min(pref[i - 1], rides[i][1])

            suff = [0] * n
            suff[-1] = rides[-1][0] + rides[-1][1]

            for i in range(n - 2, -1, -1):
                suff[i] = min(
                    suff[i + 1],
                    rides[i][0] + rides[i][1]
                )

            return starts, pref, suff

        waterStarts, waterPref, waterSuff = build(
            waterStartTime, waterDuration
        )

        landStarts, landPref, landSuff = build(
            landStartTime, landDuration
        )

        ans = inf

        # Land -> Water
        for s, d in zip(landStartTime, landDuration):
            t = s + d
            idx = bisect_left(waterStarts, t)

            if idx > 0:
                ans = min(ans, t + waterPref[idx - 1])

            if idx < len(waterStarts):
                ans = min(ans, waterSuff[idx])

        # Water -> Land
        for s, d in zip(waterStartTime, waterDuration):
            t = s + d
            idx = bisect_left(landStarts, t)

            if idx > 0:
                ans = min(ans, t + landPref[idx - 1])

            if idx < len(landStarts):
                ans = min(ans, landSuff[idx])

        return ans