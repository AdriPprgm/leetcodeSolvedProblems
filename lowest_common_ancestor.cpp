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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode *currentanc = root;
        if ((currentanc == p || currentanc == q) || !currentanc){
            return currentanc;
        }
        else{
            TreeNode *x{lowestCommonAncestor(currentanc->left,p,q)};
            TreeNode *y{lowestCommonAncestor(currentanc->right,p,q)};
            if (x && y){
                return currentanc;
            }
            else if(!x){
                return y;
            }
            else{
                return x;
            }
        }
    }
};
