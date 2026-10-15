class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[0] == '1':               
            return False
        dp = [0] * n                 
        dp[0] = 1
        pref = [0] * (n + 1)        
        pref[1] = 1                 

        for i in range(1, n):
            left = i - maxJump
            right = i - minJump

            if right >= 0:
                L = max(0, left)
                R = right
                reachable_count = pref[R + 1] - pref[L]
                if reachable_count > 0 and s[i] == '0':
                    dp[i] = 1

            pref[i + 1] = pref[i] + dp[i]

        return dp[n - 1] == 1