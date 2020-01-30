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
    bool isPalindrome(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return true;
        vector<int> list;
        while (head != nullptr) {
            list.push_back(head->val);
            head = head->next;
        }
        int left = 0;
        int right = std::size(list)-1;
        while (left < right) {
            if (list[right] != list[left]) return false;
            left++;
            right--;
        }
        return true;
    }
};