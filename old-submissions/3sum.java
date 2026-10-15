class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        
        // Edge cases
        if (nums == null || nums.length < 3) {
            return result;
        }
        
        // Sort array to handle duplicates and use two pointer technique
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicates for i to ensure unique triplets
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            // Use two pointers technique for remaining array
            int left = i + 1;
            int right = nums.length - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    // Found a triplet
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // Skip duplicates for left pointer
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    
                    // Skip duplicates for right pointer
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    
                    // Move both pointers
                    left++;
                    right--;
                } else if (sum < 0) {
                    // Sum is too small, increment left pointer
                    left++;
                } else {
                    // Sum is too large, decrement right pointer
                    right--;
                }
            }
        }
        
        return result;
    }
}