from bisect import bisect_right, insort

class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        ans = [-1] * n
        full = {}          # lake -> last rain day
        dry_days = []      # indices of 0's (sorted)
        
        for i, lake in enumerate(rains):
            if lake == 0:
                # dry day, add index to sorted dry_days
                insort(dry_days, i)
            else:
                if lake in full:
                    # find a dry day after last time this lake was filled
                    last_rain = full[lake]
                    idx = bisect_right(dry_days, last_rain)
                    if idx == len(dry_days):
                        return []  # no valid dry day → flood
                    dry_day = dry_days.pop(idx)
                    ans[dry_day] = lake  # dry this lake
                full[lake] = i  # mark lake as full
                ans[i] = -1     # raining day
        # any remaining dry days can dry any lake (say lake 1)
        for i in range(n):
            if rains[i] == 0 and ans[i] == -1:
                ans[i] = 1
        return ans
