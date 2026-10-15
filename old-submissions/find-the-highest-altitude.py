class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # prefix = [0] * len(gain)
        # prefix[0] = gain[0]

        # for i in range(1, len(gain)):
        #     prefix[i] = prefix[i - 1] + gain[i]

        # return max(prefix) if max(prefix) > 0 else 0 

        max_altitude = 0
        curr_altitude = 0

        for g in gain:
            curr_altitude += g
            if curr_altitude > max_altitude:
                max_altitude = curr_altitude

        return max_altitude
