class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        
        s2 = set()
        n = len(unique_nums)
        for i in range(n):
            for j in range(i, n):
                s2.add(unique_nums[i] ^ unique_nums[j])
                
        s3 = set()
        for val2 in s2:
            for num in unique_nums:
                s3.add(val2 ^ num)
                
        return len(s3)