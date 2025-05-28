
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1: ListNode, l2: ListNode):

		l1_rev = self.reversed_list_node(l1)
		l2_rev = self.reversed_list_node(l2)

		str_1 = self.join_ln_to_str(l1_rev)
		str_2 = self.join_ln_to_str(l2_rev)

		summ = list(str(int(str_1) + int(str_2)))
		result = [int(num) for num in reversed(summ)]
		result_ln = self.create_list_node(result)
		return result_ln

	def reversed_list_node(self, list_node):
		current_node = list_node
		prev = None
		while current_node:
			next_node = current_node.next
			current_node.next = prev
			prev = current_node
			current_node = next_node
		return prev

	def join_ln_to_str(self, list_node):
		result = ''

		while list_node:
			result += str(list_node.val)
			list_node = list_node.next

		return result

	def create_list_node(self, list):
		head = ListNode(list[0])
		tail = head
		for e in list[1:]:
			tail.next = ListNode(e)
			tail = tail.next
		return head







if __name__ == "__main__":
	l1 = [2, 4, 3]
	l2 = [5, 6, 4]

	sol = Solution()
	l1_head = sol.create_list_node(l1)
	l2_head = sol.create_list_node(l2)
	print(sol.addTwoNumbers(l1_head, l2_head))