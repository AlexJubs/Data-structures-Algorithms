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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if ((l1->next == nullptr)&&(l2->next == nullptr)) {
            if (l1->val + l2->val < 10) {
                return new ListNode(l1->val + l2-> val);
            }
            else {
                ListNode* ting = new ListNode(l1->val + l2-> val - 10);
                ting->next = new ListNode(1);
                return ting;
            }
        }
        
        vector<int> list1;
        vector<int> list2;
        int add_one{0};
        
        while (l1 != nullptr){
            list1.push_back(l1->val);
            l1 = l1->next;
        }
        while (l2 != nullptr){
            list2.push_back(l2->val);
            l2 = l2->next;
        }
        
        while (std::size(list1) != std::size(list2)){
            if (std::size(list1) < std::size(list2)){
                list1.push_back(0);
            }
            if (std::size(list2) < std::size(list1)){
                list2.push_back(0);
            }
        }
        
        ListNode* output = new ListNode(0);
        ListNode* temp = output;
        
        for (int i{0}; i < std::size(list1); i++){
            if (list1[i] + list2[i] + add_one < 10){
                output->val = list1[i] + list2[i] + add_one;
                add_one = 0;
            }
            else {
                output->val = list1[i] + list2[i] + add_one - 10;
                add_one = 1;
            }
            if (i+1 != std::size(list1)) {
                output->next = new ListNode(0);
                output = output->next;                
            }
            if ((i+1 == std::size(list1))&&(add_one == 1)){
                output->next = new ListNode(1);
            }
        }
            
        return temp;
    }
};