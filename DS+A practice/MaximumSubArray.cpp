class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = nums[0];
        int sum = 0;
        for(int i{0}; i < std::size(nums); i++){
            sum = sum + nums[i];
            ans = max(sum,ans);
            sum = max(sum,0);
        }
        return ans;
    }
};