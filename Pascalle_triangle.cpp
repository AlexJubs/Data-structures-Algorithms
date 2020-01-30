class Solution {
public:
    vector<int> getRow(int numRows) {
        vector<vector<int>> output;
        if (numRows == 0) return {1};
        else if (numRows >= 1) {
            output.push_back({1});
            output.push_back({1,1});
            if (numRows == 1) return {1,1};
        }
        vector<int> temp;
        while (std::size(output) <= numRows) {
            for (int i{0}; i <= std::size(output); i++) {
                if (i == 0 || i == std::size(output)) temp.push_back(1);
                else temp.push_back(output[std::size(output)-1][i-1]
                                    + output[std::size(output)-1][i]);
            }
            output.push_back(temp);
            temp = {};
        }
        return output[std::size(output)-1];
    }
};