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
    bool hasCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr) return false;
        ListNode* p1 = head;
        ListNode* p2 = head->next;
        while (p1 != nullptr && p2 != nullptr) {
            if (p1 == p2) return true;
            p1 = p1->next;
            if (p2->next == nullptr) break;
            p2 = p2->next->next;
        }
        return false;
    }
};