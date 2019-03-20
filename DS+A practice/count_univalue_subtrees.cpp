class Solution {
public:
    bool isLeafNode(TreeNode* root) {
        if (root->left == nullptr && root->right == nullptr) return true;
        return false;
    }
    int countUnivalSubtrees(TreeNode* root) {
        if (root == nullptr) return 0;
        if (root->right == nullptr && root->left == nullptr) return 1;
        if (root->left == nullptr && root->right != nullptr) {
            if (root->right->val == root->val && isLeafNode(root->right)) return countUnivalSubtrees(root->right) +1;
            else return countUnivalSubtrees(root->right);
        }
        if (root->left != nullptr && root->right == nullptr) {
            if (root->left->val == root->val && isLeafNode(root->left)) return countUnivalSubtrees(root->left) +1;
            else return countUnivalSubtrees(root->left);    
        }
        if (root->left != nullptr && root->right != nullptr) {
            if (root->left->val == root->right->val && root->val == root->left->val){
                return countUnivalSubtrees(root->left) + countUnivalSubtrees(root->right) +1;
            }
            else return countUnivalSubtrees(root->left) + countUnivalSubtrees(root->right);
        }
        return 1;
    }
};