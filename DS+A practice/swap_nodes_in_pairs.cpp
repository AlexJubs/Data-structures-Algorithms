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
    ListNode* swapPairs(ListNode* head) {
        ListNode* tempPtr;
        int counter{0};
        tempPtr = head;
        
        while(head != nullptr){
            if ((counter%2 == 0)&&(head->next != nullptr)){
                std::swap(head->val, head->next->val);
            }
            std::cout << head->val << std::endl;
            
            head = head->next;
            counter++;
        }
        
        return tempPtr;
    }
};