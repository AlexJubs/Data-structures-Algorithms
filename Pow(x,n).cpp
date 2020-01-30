#include <cstdlib>

class Solution {
public: 
    double myPow(double x, int n) {
        if ((n==0)||(x==1)){
            return 1.0;
        }
        if (x == -1) {
            if (n%2 == 1){return -1.0;}
            else {return 1.0;}
        }
        
        if (n == -2147483648) {
            return 0.0;
        }
        
        double num {1};
        
        for (int i{0}; i < abs(n); i++){
            num = num*x;
        }
        
        if (n > 0){return (num);}
        else {return (1/num);}
        
        return 0.0;
    }
}