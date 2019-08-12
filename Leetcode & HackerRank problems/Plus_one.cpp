class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        if (std::size(digits) == 0) return {};
        if (std::size(digits) == 1 && digits[0] == 9) return {1,0};
        for (int i{0}; i < std::size(digits); i++) {
            if (digits[i] != 9) break;
            if (i == std::size(digits)-1) {
                digits.push_back(0);
                digits[0] = 1;
                for (int j{1}; j <= std::size(digits); j++) digits[j] = 0;
                return digits;
            }
        }
        
        digits[std::size(digits)-1] = digits[std::size(digits)-1] + 1;
        if (digits[std::size(digits)-1] < 10) return digits;
        else {
            int j = std::size(digits) -1;
            for (int i{std::size(digits)-1}; i >= 0; i--) {
                if (digits[i] == 10) {
                    digits[i] = 0;
                    digits[i-1] = digits[i-1] +1;
                }
            }
        }
        
        return digits;
    }
};