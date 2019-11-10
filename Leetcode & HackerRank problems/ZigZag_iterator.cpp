#include <queue>

class ZigzagIterator {
public:
    queue<int> q1;
    queue<int> q2;
    int counter = 0;
    int ret;
    
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        for (int i{0}; i < v1.size(); i++) q1.push(v1[i]);
        for (int i{0}; i < v2.size(); i++) q2.push(v2[i]);
    }
    
    int next() {
        if (q1.empty()) {
            ret = q2.front();
            q2.pop();
            return ret;
        }
        if (q2.empty()) {
            ret = q1.front();
            q1.pop();
            return ret;
        }
        if (counter % 2 == 0) {
            counter++;
            ret = q1.front();
            q1.pop();
            return ret;
        }
        if (counter % 2 == 1) {
            counter++;
            ret = q2.front();
            q2.pop();
            return ret;
        }
        return -1;
    }
    
    bool hasNext() {
        return q1.empty() == false || q2.empty() == false;
    }
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */