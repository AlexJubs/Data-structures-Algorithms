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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) return true;
        if ((p == nullptr && q != nullptr) || (p != nullptr && q == nullptr)) return false;
        if (q->val != p->val) return false;
        else return (isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
        
    }
};