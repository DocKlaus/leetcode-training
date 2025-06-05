class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        print(current)

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next

    def create_list_node(self, list):
        head = ListNode(list[0])
        tail = head
        for e in list[1:]:
            tail.next = ListNode(e)
            tail = tail.next
        return head


list1 = [1, 2, 4]
list2 = [1, 3, 4]
sol = Solution()
l1_head = sol.create_list_node(list1)
l2_head = sol.create_list_node(list2)
print(sol.mergeTwoLists(l1_head, l2_head))
