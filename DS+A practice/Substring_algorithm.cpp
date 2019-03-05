class Solution {
public:
    bool HasDuplicates (string s) {   
        for (int i = 0; i < s.length(); i++) {
            for (int j = i+1; j < s.length(); j++) {
              if (s[i] == s[j])
                return true;   
            }
        }
        return false;
    }
    
    int lengthOfLongestSubstring(string s) {
        if (std::size(s) == 0){return 0;}
        if (std::size(s) == 1){return 1;}
        if (HasDuplicates(s) == false){return std::size(s);}
        
        vector<string> array;
        for (int i{0}; i <= std::size(s); i++){
            for (int j{0}; j <= std::size(s); j++){
                if ((s.substr(i,j) != "")&&(HasDuplicates(s.substr(i,j)) == false)){
                    array.push_back(s.substr(i,j));
                }
            }
        }
        
        int l{0};
        for (int i{0}; i < std::size(array); i++) {
            if (std::size(array[i]) > l){
                l = std::size(array[i]);
            }
        }
        
        return l;
    }
};