/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <stdlib.h>
class Solution {
public:
    ListNode* head;
    int len = 0;
    int trav;
    ListNode* runner;
    ListNode* top;
    
    Solution(ListNode* head) {
        ListNode* temp = head;
        top = head;
        while (temp != NULL) {
            temp = temp->next;
            len++;
        }
        len = move(len);
        head = move(head);
    }
    
    int getRandom() {
        runner = top;
        trav = rand() % len;
        while (trav > 0) {
            if (runner->next == NULL) break;
            runner = runner->next;
            trav = trav-1;
        }
        return runner->val;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */