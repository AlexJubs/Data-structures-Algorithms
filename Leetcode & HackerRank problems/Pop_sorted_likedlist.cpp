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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == nullptr){return nullptr;}
        ListNode* trav = head;
        while (trav->next != nullptr){trav = trav->next;}
        int value = trav->val+1-n;
        if (value == 1){
            return head->next;
        }
        ListNode* temp;
        ListNode* output = head;
        while (head != nullptr){
            if ((head->next != nullptr)&&(head->next->val == value)){
                head->next = head->next->next;
            }
            head = head->next;
        }
        return output;
    }
};