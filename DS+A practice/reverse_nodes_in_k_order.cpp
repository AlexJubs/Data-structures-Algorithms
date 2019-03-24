#include <vector>
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == nullptr || head->next == nullptr || k == 1) return head;
        vector<int> nums;
        for (int i{0}; head != nullptr; head = head->next) nums.push_back(head->val);
        int top;
        int limit = std::size(nums) - std::size(nums)%k;
        for (int i{0}; i < limit; i = i+k) {
            top = i+k-1;
            for (int j{i}; j < top; j++) {
                std::swap(nums[j], nums[top]);
                top--;
            }
        }
        
        ListNode* temp = new ListNode(nums[0]);
        ListNode* output = temp;
        for (int i{1}; i < std::size(nums); i++) {
            temp->next = new ListNode(nums[i]);
            temp = temp->next;
        }
        return output;
    }
};