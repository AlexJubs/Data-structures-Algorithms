class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        if (std::size(nums) == 0) {return 0;}
        if (std::size(nums) < 3) {return nums[0];}
        for (int i{0}; i < std::size(nums); i++) {
            for (int j{0}; j < std::size(nums); j++) {
                if ((nums[i] == nums[j]) && (i != j)) {
                    return nums[i];
                }
            }
        }
        return 0;
    }
};