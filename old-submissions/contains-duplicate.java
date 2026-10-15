class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> dups = new HashSet<Integer>();
        for (int n : nums) {
            if (dups.contains(n)) {
                return true;
            }
            dups.add(n);
        }
        return false;
    }
}