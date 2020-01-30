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
    int output;
    int countNodes(TreeNode* root) {
        if (root != nullptr) {
            output++;
            countNodes(root->right);
            countNodes(root->left);
        }
        return output;
    }
};