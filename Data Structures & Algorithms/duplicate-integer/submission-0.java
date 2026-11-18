class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> new_set = new HashSet<Integer>();
        for(int j : nums){
            if (!new_set.contains(j)){
                new_set.add(j);
            }else{
                return true;
            }
        }
        return false;
    }
}