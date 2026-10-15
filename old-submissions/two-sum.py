class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in index_map:
                return [index_map[diff], i]

            index_map[num] = i
