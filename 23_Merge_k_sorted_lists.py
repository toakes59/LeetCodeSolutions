# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i))
                lists[i] = node.next
        
        dummy = ListNode()
        current = dummy

        while heap:
            val, idx = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next

            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return dummy.next