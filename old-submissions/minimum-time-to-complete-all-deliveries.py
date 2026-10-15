class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        d1, d2 = d[0], d[1]
        r1, r2 = r[0], r[1]

        total_deliveries = d1 + d2

        lcm = (r1 * r2) // gcd(r1, r2)

        low = total_deliveries
        high = 2 * total_deliveries

        ans = high

        while low <= high:
            mid = (low + high) // 2

            slots1 = mid - (mid // r1)
            slots2 = mid - (mid // r2)

            total_slots = mid - (mid // lcm)

            if (slots1 >= d1 and slots2 >= d2 and total_slots >= total_deliveries):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans