
def isValid(s):
	if len(s) % 2 != 0:
		return False
	elements = {
		'(': ')',
		'{': '}',
		'[': ']'
		}
	set_clos = {')', '}', ']'}
	stack = []
	for char in s:
		if char in elements:
			stack.append(char)
		elif char in set_clos:
			if len(stack) == 0 or elements[stack[-1]] != char:
				return False
			else:
				stack.pop()

	return len(stack) == 0




s = "([])"
print(isValid(s))