class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        sample = ListNode(0)
        sample.next = head
        right = left = sample

        for _ in range(n + 1):
            right = right.next

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return sample.next

    def create_list_node(self, list):
        head = ListNode(list[0])
        tail = head
        for e in list[1:]:
            tail.next = ListNode(e)
            tail = tail.next
        return head


head = [1, 2, 3, 4, 5]
n = 2
sol = Solution()
l1_head = sol.create_list_node(head)
print(sol.removeNthFromEnd(l1_head, n))
