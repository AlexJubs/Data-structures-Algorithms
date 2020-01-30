class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (std::size(matrix) == 0 || std::size(matrix[0]) == 0) return false;
        if (target < matrix[0][0] || target > matrix[std::size(matrix)-1][std::size(matrix[0])-1]) {
            return false;
        }
        vector<int> set;
        for (int i{0}; i < std::size(matrix); i++) {
            if (matrix[i][0] <= target && matrix[i][std::size(matrix[0])-1] >= target){
                set.push_back(i);
            }
            if (matrix[i][0] > target) break;
        }
        if (std::size(set) == 0) return false;
        for (int j{set[0]}; j <= set[std::size(set)-1]; j++) {
            for (int k{0}; k < std::size(matrix[j]); k++) {
                if (matrix[j][k] == target) return true;
                if (matrix[j][k] > target) break;
            }
        }
        return false;
    }
};