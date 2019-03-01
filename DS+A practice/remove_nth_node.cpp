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
        ListNode* output = head;
        int counter{0};
        while(trav != nullptr){
            counter++;
            trav = trav->next;
        }
        if ((counter-n == 1)&&counter<3){
            head->next = nullptr;
            return head;
        }
        if (counter == n){
            return head->next;
        }
        for (int i{0}; i < counter-n-1; i++){
            head = head->next;
        }
        head->next = head->next->next;

        return output;
    }
};