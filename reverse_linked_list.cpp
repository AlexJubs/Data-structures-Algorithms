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
    vector<int> reverseArray(vector<int> input){
        int low = 0;
        int high = std::size(input)-1;
        while (low < high) {
            std::swap(input[low], input[high]);
            low++;
            high--;
        }
        return input;
    }
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) return nullptr;
        vector<int> list;
        ListNode* temp = head;
        while (temp != nullptr) {
            list.push_back(temp->val);
            temp = temp->next;
        }
        list = reverseArray(list);
        ListNode* output = head;
        for (int i{0}; i < std::size(list); i++) {
            head->val = list[i];
            head = head->next;
        }
        return output;
    }
};