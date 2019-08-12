class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (std::size(strs) == 0) {return "";}
        if (std::size(strs) == 1) {return strs[0];}
        
        int len{0};
        bool Go {true};
        while ((Go == true)) {
            for (int i{0}; i < std::size(strs) - 1; i++) {
                if (strs[i] == "") {return "";}
                if (len >= std::size(strs[i]) || (len >= std::size(strs[i+1]))) {
                    Go = false;
                    break;
                }
                if (strs[i][len] != strs[i+1][len]){Go = false;}
            }
            len++;
        }
        if (len == 0) {return "";}
        return (strs[0].substr(0,len-1));
    }
};