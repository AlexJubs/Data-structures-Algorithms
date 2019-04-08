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
    ListNode* oddEvenList(ListNode* head) {
        if (head == nullptr || head->next == nullptr || head->next->next == nullptr) return head;
        int counter{1};
        ListNode* odd = new ListNode(head->val);
        ListNode* even = new ListNode(head->next->val);
        ListNode* temp = even;
        ListNode* output = odd;
        head = head->next->next;
        while (head != nullptr) {
            if (counter%2 == 1) {
                odd->next = new ListNode(head->val);
                odd = odd->next;
            }
            if (counter%2 == 0) {
                even->next = new ListNode(head->val);
                even = even->next;
            }
            counter++;
            head = head->next;
        }
        odd->next = temp;
        return output;
    }
};