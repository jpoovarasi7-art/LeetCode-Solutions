/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        // Base case: if list is empty or has only one node, no swap needed
        if (head == null || head.next == null) {
            return head;
        }

        // Dummy node simplifies pointer operations before head
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prev = dummy;

        while (prev.next != null && prev.next.next != null) {
            // Identify the two nodes to swap
            ListNode first = prev.next;
            ListNode second = prev.next.next;

            // Perform pointer adjustments
            first.next = second.next;
            second.next = first;
            prev.next = second;

            // Move prev two steps forward for the next iteration
            prev = first;
        }

        return dummy.next;
    }
}