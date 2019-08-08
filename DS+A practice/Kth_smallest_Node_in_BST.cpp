/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> arr;
    int kthSmallest(TreeNode* root, int k) {
        if (root == nullptr) return 0;
        arr = {};
        inOrder(root);
        return arr[k-1];
    }
    void inOrder(TreeNode* root) {
        if (root != nullptr) {
            inOrder(root->left);
            arr.push_back(root->val);
            inOrder(root->right);
        }
    }
};