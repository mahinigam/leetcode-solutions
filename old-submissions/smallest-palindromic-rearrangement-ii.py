class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)
        
        odd_count = sum(1 for v in count.values() if v % 2 == 1)
        if odd_count > 1:
            return ""
            
        half_count = [0] * 26
        mid_letter = ""
        for c, freq in count.items():
            idx = ord(c) - 97
            half_count[idx] = freq // 2
            if freq % 2 == 1:
                mid_letter = c
                
        def get_comb(n, r):
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res > 1000000:
                    return 1000001
            return res

        def count_arrangements(counts):
            total = sum(counts)
            res = 1
            for freq in counts:
                if freq == 0:
                    continue
                res *= get_comb(total, freq)
                if res > 1000000:
                    return 1000001
                total -= freq
            return res

        if k > count_arrangements(half_count):
            return ""
            
        left_half = []
        half_len = sum(half_count)
        
        for _ in range(half_len):
            for i in range(26):
                if half_count[i] == 0:
                    continue
                
                half_count[i] -= 1
                arrangements = count_arrangements(half_count)
                
                if k <= arrangements:
                    left_half.append(chr(i + 97))
                    break
                else:
                    k -= arrangements
                    half_count[i] += 1
                    
        return "".join(left_half) + mid_letter + "".join(reversed(left_half))