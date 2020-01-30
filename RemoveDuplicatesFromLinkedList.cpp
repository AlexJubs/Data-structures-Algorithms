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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;
        if (head->next->val == head->val) {
            head = head->next;
            return deleteDuplicates(head);
        }
        head->next = deleteDuplicates(head->next);
        return head;
    }
};