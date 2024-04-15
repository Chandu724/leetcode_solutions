/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode RemoveElements(ListNode head, int val) {
     ListNode cur=head;
        while(head!=null && head.val==val) head = head.next;
       while(cur!=null && cur.next!=null){
             if(cur.next.val != val)
               cur= cur.next;
           else{
               cur.next = cur.next.next;
           }
         
         
       }
        return head;
    }
}


            //return head;