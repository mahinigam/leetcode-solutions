class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        best_rules = {}
        for (p, r), c in zip(rules, costs):
            total_cost = c + p.count('*')
            if (r, p) not in best_rules or total_cost < best_rules[(r, p)]:
                best_rules[(r, p)] = total_cost

        rules_by_target = {}
        for (r, p), c in best_rules.items():
            if r not in rules_by_target:
                rules_by_target[r] = []
            rules_by_target[r].append((p, c))

        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n+1):
            if source[i-1] == target[i-1]:
                dp[i] = dp[i-1]

            for L in range(1, min(20, i) + 1):
                t_sub = target[i-L : i]

                if t_sub in rules_by_target:
                    s_sub = source[i-L : i]

                    for p, c in rules_by_target[t_sub]:
                        if dp[i-L] + c < dp[i]:
                            match = True
                            for j in range(L):
                                if p[j] != '*' and p[j] != s_sub[j]:
                                    match = False
                                    break

                            if match:
                                dp[i] = dp[i-L] + c

        return dp[n] if dp[n] != float('inf') else -1