#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the rotLeft function below.
vector<int> rotLeft(vector<int> a, int d) {
    vector<int> b (a.size());
    d = d%a.size();
    if (d == 0) return a;
    int index;
    for (int i{a.size()-1}; i >= 0; i--) {
        index = (i-d);
        if (index < 0) index = index+a.size();
        b[index] = a[i];
    }
    return b;
}