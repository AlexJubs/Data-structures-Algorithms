class Solution {
public:
    vector<int> cand = {};
    vector<vector<int>> res = {};
    void helper (int target, vector<int> arr, int p1) {
        if (target < 0) return;
        if (target == 0) {
            res.push_back(arr);
            return;
        }
        if (p1 >= cand.size()) return;
        helper(target,arr, p1+1);
        
        arr.push_back(cand[p1]);
        helper(target-cand[p1],arr,p1);
        helper(target-cand[p1],arr,p1+1);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        if (target == 0) return {{}};
        cand = move(candidates);
        helper(target, {}, 0);
        return res;
    }
};