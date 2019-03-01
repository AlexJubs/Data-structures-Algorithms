class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int difference;
        int minimum{2147483647};
        int sum;
        for (int i{0}; i < std::size(nums); i++){
            for (int j{0}; j < std::size(nums); j++){
                for (int k{0}; k < std::size(nums); k++){
                    if ((i != j) and (i != k) and (k != j)){
                        difference = abs(target - (nums[i] + nums[j] + nums[k]));
                        if (difference < minimum){
                            minimum = difference;
                            sum =  nums[i] + nums[j] + nums[k];
                        }    
                    }
                }
            }
        }
        return sum;
    }
};