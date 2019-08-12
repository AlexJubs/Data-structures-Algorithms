class Solution {
public:
    string addBinary(string a, string b) {
        if (std::size(a) == 0) return b;
        if (std::size(b) == 0) return a;
        string output = "";
        int Ac = std::size(a);
        int Bc = std::size(b);
        bool carry = false;
        int X;
        int Y;
        while (Ac >= 0 || Bc >= 0) {
            
            if (Ac >= 0) X = a[Ac];
            else X = '0';
            if (Bc >= 0) Y = b[Bc];
            else Y = '0';
            
            if (X == '0' && Y == '0') {
                if (carry == true) {
                    output = '1' + output;
                    carry = false;
                }
                else output = "0" + output;
            }
            else if((X == '0' && Y == '1') || (X == '1' && Y == '0')) {
                if (carry == true) {
                    output = '0' + output;
                    carry = true;
                }
                else {
                    output = "1" + output;
                    carry = false;
                }
            }
            if (X == '1' && Y == '1') {
                if (carry == true) {
                    output = '1' + output;
                    carry = true;
                }
                else {
                    output = "0" + output;
                    carry = true;
                }
            }
            Ac--;
            Bc--;
        }
        if (carry == true) output = '1' + output;
        return output;
    }
};