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
        int size{0};

        ListNode* l3 = l2;
        
        while (l3 != nullptr){
            size = size+1;
            l3 = l3->next;
        }
        
        int num1[size], num2[size], num3[size], counter{0};
        std::stringstream ss1, ss2;
        
        std::cout<<"number 1:"<<std::endl;
        
        while ((l1 != nullptr)&&(size>1)){
            num1[size-1-counter] = l1->val;
            l1 = l1->next;
            counter = counter+1;
        }
        counter = 0;
                
        for (int i{0}; i < size; i++){
            std::cout<<num1[i];
            ss1 << num1[i];
        }
        
        std::cout<<std::endl<<"number 2:"<<std::endl;
        
        while ((l2 != nullptr)&&(size>1)){
            num2[size-1-counter] = l2->val;
            l2 = l2->next;
            counter = counter+1;
        }
        counter = 0;
        
        for (int i{0}; i < size; i++){
            std::cout<<num2[i];
            ss2 << num2[i];
        }
        
        std::cout<<std::endl<<"Number to be outputed:"<<std::endl;
        
        int number1, number2;
        ss1 >> number1;
        ss2 >> number2;
        int output_number = number1+number2;
            
        std::cout << output_number<<std::endl;
        
        int output_array[size];
        for (int i = 0; i < size; i++) {
            output_array[i] = output_number%10;
            output_number = output_number/10;
        }
        
        std::cout<<"Output array:"<<std::endl;
        
        for(int i = 0; i < size; i++){
            std::cout<<output_array[i];
            
        }
        
        ListNode* ans = new ListNode(output_array[0]);
        ListNode* trav = ans;

        for(int i=1;i<size;i++){
            trav->next = new ListNode(output_array[i]);
            trav = trav->next;
        }
        
        return ans;
    }
};