class Solution {
public:
        
    int missingNumber(vector<int>& nums) {
        if ((std::size(nums) == 1) && (nums[0] == 0)) {return 1;}
        
        sort(nums.begin(),nums.end());
        
        for (int i{0}; i < std::size(nums); i++) {
            if (i != nums[i]){
                return i;
            }
        }
        return nums[std::size(nums)-1]+1;
    }
};