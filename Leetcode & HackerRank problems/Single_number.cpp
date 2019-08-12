class Solution {
public:
    int singleNumber(vector<int>& nums) {
        if (std::size(nums) == 1) return nums[0];
        sort(nums.begin(), nums.end());
        if (nums[0] != nums[1]) return nums[0];
        if (nums[std::size(nums)-1] != nums[std::size(nums)-2]) {
            return nums[std::size(nums)-1];
        } 
        for (int i{1}; i < nums.size()-1; i++) {
            if (nums[i] != nums[i+1] && nums[i] != nums[i-1]) return nums[i];
        }
        return -1;
    }
};