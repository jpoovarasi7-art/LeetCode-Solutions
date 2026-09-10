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
    bool hasCycle(ListNode *head) {
        ListNode *temp = head;
        if(head==NULL || head->next==NULL)
        {
            return false;
        }
        ListNode *sam = head;
        while(sam!=NULL && sam->next!=NULL)
        {
            sam=sam->next->next;
            temp = temp->next;
            if(sam==temp)
            {
                return true;
            }
        }
        return false;
    }
};