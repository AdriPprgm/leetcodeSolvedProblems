/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head){
            return head;
        }
        int size = 1;
        ListNode *current = head;
        while(current->next){
            current = current->next;
            size++;
        }
        for (int i{0}; i < k%size; ++i){
            ListNode *current = head;
            ListNode *prevLast = head;
            while(current->next){
                prevLast = current;
                current = current->next;
            }
            current->next = head;
            prevLast->next = nullptr;
            head = current;
        }
        return head;
    }
};