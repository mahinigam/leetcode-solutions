class Solution:
    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
        
    def completePrime(self, num: int) -> bool:
        s = str(num)
        n = len(s)

        for i in range(1, n+1): # All prefixes
            if not self.isPrime(int(s[:i])):
                return False

        for i in range(n): # All suffixes
            if not self.isPrime(int(s[i:])):
                return False

        return True
        