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
    ListNode *detectCycle(ListNode *head) {
        ListNode *temp = head;
        if(head==NULL || head->next==NULL)
        {
            return 0;
        }
        ListNode *sam = head;
        ListNode *sam1 = head;
        bool is_cycle = false;
        while(sam!=NULL && sam->next!=NULL)
        {
            sam=sam->next->next;
            temp = temp->next;
            if(sam==temp)
            {
                is_cycle = true;
                break;
            }
        }
        if(!is_cycle)
            {
                return NULL;
            }
            while(sam1!=temp)
            {
                sam1=sam1->next;
                temp = temp->next;
            }
        return sam1;
    }
};