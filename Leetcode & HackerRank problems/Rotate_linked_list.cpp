ListNode* shift(ListNode* head) {
        ListNode* tail = head;
        while (tail->next != nullptr) {
            tail = tail->next;
        }
            
        ListNode* trav = head;
        ListNode* output = trav;
        int temp = tail->val;

        while (trav != nullptr) {
            std::swap(temp,trav->val);
            trav = trav->next;
        }
        
                
        return output;
    }
    
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr) return nullptr;
        while (k > 0) {
            shift(head);
            k = k-1;
        }
        return head;
}