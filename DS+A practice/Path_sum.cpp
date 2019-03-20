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
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == nullptr) return false;
        sum = sum - root->val;
        if (root->left == nullptr && root->right == nullptr) {
            if (sum == 0) return true;
            else return false;
        }
        return hasPathSum(root->left,sum) || hasPathSum(root->right,sum);
    }
};