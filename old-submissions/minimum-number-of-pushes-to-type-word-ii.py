class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        
        freqs = sorted(counts.values(), reverse=True)
        
        ans = 0
        
        for i, freq in enumerate(freqs):
            pushes_per_char = (i // 8) + 1
            ans += freq * pushes_per_char
            
        return ans