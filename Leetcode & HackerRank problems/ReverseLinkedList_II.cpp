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
    vector<int> reverseVec(vector<int> nums, int m, int n) {
        while (m < n) {
            std::swap(nums[m], nums[n]);
            m++;
            n--;
        }
        return nums;
    }
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        vector<int> nums;
        while (head != nullptr) {
            nums.push_back(head->val);
            head = head->next;
        }
        nums = reverseVec(nums, m-1, n-1);
        ListNode* output = new ListNode(nums[0]);
        ListNode* ACTUALOUTPUT = output;
        for (int i{1}; i < std::size(nums); i++) {
            output->next = new ListNode(nums[i]);
            output = output->next;
        }
        return ACTUALOUTPUT;
    }
};