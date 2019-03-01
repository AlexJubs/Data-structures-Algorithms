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
    ListNode* sortList(ListNode* head) {
        if (head == nullptr){return nullptr;}
        ListNode* temp = head;
        ListNode* ting = head;
        ListNode* output = temp;
        
        while (ting->next != nullptr){
            while (temp->next != nullptr){
                if (temp->next->val < temp->val){
                    std::swap(temp->next->val, temp->val);
                }
                temp = temp->next;
            }
            temp = head;
            ting = ting->next;
        }
        
        return output;
    }
};