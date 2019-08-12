class Solution {
public:    
    void sortColors(vector<int>& nums) {
        for (int gap = std::size(nums)/2; gap > 0; gap = gap/2) {
            for (int i = gap; i < std::size(nums); i++) { 
                int temp = nums[i];
                int j;             
                for (j = i; j >= gap && nums[j - gap] > temp; j -= gap) {
                    nums[j] = nums[j - gap];
                }
                nums[j] = temp; 
            } 
        }
    }
};