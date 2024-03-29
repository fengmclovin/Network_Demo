class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode prev = dummy;
        ListNode curr = head;
        
        while (curr != null) {
            ListNode tail = curr;
            
            // Check if there are k nodes remaining
            int count = 0;
            while (curr != null && count < k) {
                curr = curr.next;
                count++;
            }
            
            if (count == k) {
                // Reverse the sublist of size k
                ListNode reversedSublist = reverseList(tail, k);
                
                // Update the pointers
                prev.next = reversedSublist;
                prev = tail;
            } else {
                // No need to reverse, break the loop
                break;
            }
        }
        
        return dummy.next;
    }
    
    private ListNode reverseList(ListNode head, int k) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (k > 0) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
            k--;
        }
        
        return prev;
    }
}
