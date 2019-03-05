class Solution {
public:
    int trap(vector<int>& height) {
        if (std::size(height) == 0) {return 0;}
        int output{0};
        vector <int> left_max(std::size(height));
        vector <int> right_max(std::size(height));
        
        left_max[0] = height[0];
        for (int i{1}; i < std::size(height); i++) {left_max[i] = max(height[i], left_max[i-1]);}
        
        right_max[std::size(height)-1] = height[std::size(height)-1];
        for (int i{std::size(height)-2}; i >= 0; i--) {right_max[i] = max(height[i], right_max[i+1]);}
        

        for (int i{0}; i < std::size(height); i++) {output = output + min(left_max[i], right_max[i]) - height[i];}

        
        return output;
    }
};