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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (std::size(lists) == 0){return nullptr;} 
        vector<int> arr;
        for (int i{0}; i < std::size(lists); i++){
            ListNode* temp = lists[i];
            while (temp != nullptr){
                arr.push_back(temp->val);
                temp = temp->next;
            }
        }
        if (std::size(arr) == 0) {return nullptr;}
        std::sort(arr.begin(), arr.end());
        ListNode* output = new ListNode(0);
        output->val = arr[0];
        ListNode* ting = output;
        for (int i{0}; i < std::size(arr)-1; i++){
            output->next = new ListNode(arr[i+1]);
            output = output->next;
        }
        return ting;
    }
};