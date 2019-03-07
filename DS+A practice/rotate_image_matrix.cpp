class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for (int i{0}; i < std::size(matrix); i++) {
            for (int j{i}; j < std::size(matrix); j++) {
                std::swap(matrix[i][j], matrix[j][i]);
            }
        }
        for (int i{0}; i < std::size(matrix); i++) {
            std::reverse(matrix[i].begin(),matrix[i].end());
        }
    }
};