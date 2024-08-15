class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)

        while cur.next:

            if cur.next.val == val:

                cur.next = cur.next.next  

            else:

                cur = cur.next  

        return dummy.next
