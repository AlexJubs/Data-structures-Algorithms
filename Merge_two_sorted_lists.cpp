/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if ((l1 == nullptr) && (l2 == nullptr)){return nullptr;}
        
        std::vector<int> arr;
        ListNode* temp = new ListNode(0);
        ListNode* output = temp;
        
        while (l1 != nullptr){
            arr.push_back(l1->val);
            l1 = l1->next;
        }
        
        while (l2 != nullptr){
            arr.push_back(l2->val);
            l2 = l2->next;
        }
        
        std::sort (arr.begin(), arr.end());
        temp->val = arr[0];
        for (int i{0}; i < std::size(arr)-1; i++){
            temp->next = new ListNode(arr[i+1]);
            temp = temp->next;
        }
        
        return output;
    }
};