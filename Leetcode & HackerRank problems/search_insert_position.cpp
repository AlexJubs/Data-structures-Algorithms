class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums[0] > target){return 0;}
        if (nums[std::size(nums)-1] < target){return std::size(nums);}
        for (int i{0}; i < std::size(nums); i++){
            if (nums[i] >= target) {
                return i;
            }
        }
        return 0;
    }
};