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
    int height(TreeNode* root) {
        if (root != nullptr) {
            return std::max(height(root->left), height(root->right)) +1;
        }
        return 0;
    }
    bool isBalanced(TreeNode* root) {
        if (root == nullptr || (root->left == nullptr && root->right == nullptr)) return true;
        int lh = height(root->left);
        int rh = height(root->right);
        if (abs(lh-rh) < 2 && isBalanced(root->right) && isBalanced(root->left)) return true;
        return false;
    }
};