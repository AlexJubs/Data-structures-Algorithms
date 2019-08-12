class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> output;
        int com;
        for (int i{0}; i < std::size(nums); i++) {
            com = target - nums[i];
            if (com >= nums[i]) {
                for (int j{i+1}; j < std::size(nums); j++) {
                    if (com == nums[j]) {
                        output.push_back(i+1);
                        output.push_back(j+1);
                        return output;
                    }
                }
            }
        }
        return output;
    }
};