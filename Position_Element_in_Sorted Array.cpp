class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        std::vector<int> a;
        vector<int> b{-1,-1};
        for (int i{0}; i < std::size(nums); i++) {
            if (nums[i] == target){
                a.push_back(i);
            }
        }
        if (std::size(a) == 0){return b;}
        else{
            std::vector<int> output {a[0], a[std::size(a)-1]};
            return output;
        }
    }
};