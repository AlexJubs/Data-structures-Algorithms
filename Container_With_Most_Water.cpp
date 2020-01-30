class Solution {
public:
    int maxArea(vector<int>& height) {
        int output{0};
        for (int i{0}; i < std::size(height); i++) {
            for (int j{i+1}; j < std::size(height); j++) {
                if (abs(i-j)*std::min(height[i], height[j]) > output) output = abs(i-j)*std::min(height[i], height[j]);
            }
        }
        return output;
    }
};