from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for head in lists:
            current = head
            while current:
                nodes.append(current)
                current = current.next

        nodes.sort(key=lambda x: x.val)

        dummy = ListNode(0)
        current = dummy
        for node in nodes:
            current.next = node
            current = current.next
        current.next = None

        return dummy.next
