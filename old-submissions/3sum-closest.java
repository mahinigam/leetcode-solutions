class Solution {
    public int threeSumClosest(int[] nums, int target) {
        // Sort array to use two pointer technique
        Arrays.sort(nums);
        
        // Initialize closest sum with first three elements
        int closestSum = nums[0] + nums[1] + nums[2];
        
        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicates for i to improve efficiency
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            // Use two pointers for remaining elements
            int left = i + 1;
            int right = nums.length - 1;
            
            while (left < right) {
                int currentSum = nums[i] + nums[left] + nums[right];
                
                // Update closestSum if current sum is closer to target
                if (Math.abs(currentSum - target) < Math.abs(closestSum - target)) {
                    closestSum = currentSum;
                }
                
                // If we found exact sum, return immediately
                if (currentSum == target) {
                    return target;
                }
                
                if (currentSum < target) {
                    // Current sum is too small, increment left pointer
                    left++;
                } else {
                    // Current sum is too large, decrement right pointer
                    right--;
                }
            }
        }
        
        return closestSum;
    }
}