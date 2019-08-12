class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if (std::size(nums) == 0) return;
        int temp;
        for (int j{0}; j < k; j++) {
            temp = nums[std::size(nums)-1];
            for (int i{0}; i < std::size(nums); i++) {
                std::swap(nums[i], temp);
            }
        }
    }
};