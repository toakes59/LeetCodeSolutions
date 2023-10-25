# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head, k):
            prev = None
            current = head
            while k > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1
            return prev

        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        length = getLength(head)
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        while length >= k:
            group_start = prev_group_end.next
            group_end = group_start
            for _ in range(k-1):
                group_end = group_end.next

            next_group_start = group_end.next
            group_end.next = None
            prev_group_end.next = reverseLinkedList(group_start, k)
            group_start.next = next_group_start
            prev_group_end = group_start
            length -= k

        return dummy.next

