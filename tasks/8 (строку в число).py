def myAtoi(s):
	s = s.strip()
	if not s:
		return 0

	sign = 1
	if s[0] == '-':
		sign = -1
		s = s[1:]
	elif s[0] == '+':
		s = s[1:]

	s = s.lstrip('0')
	if not s:
		return 0

	result = 0
	INT_MAX = 2 ** 31 - 1  # 2147483647
	INT_MIN = -2 ** 31  # -2147483648

	for char in s:
		if not char.isdigit():
			break

		digit = int(char)

		if sign == 1 and (result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
			return INT_MAX

		elif sign == -1 and (
				result > abs(INT_MIN) // 10 or (result == abs(INT_MIN) // 10 and digit > abs(INT_MIN) % 10)):
			return INT_MIN

		result = result * 10 + digit

	result *= sign

	return max(INT_MIN, min(result, INT_MAX))


def myAtoi1(self, s):
	"""
	:type s: str
	:rtype: int
	если результат может выходить за рамки предела, но вывод требует ограничения, можно сократить проверки
	"""
	s = s.strip()
	if not s:
		return 0

	sign = 1
	if s[0] == '-':
		sign = -1
		s = s[1:]
	elif s[0] == '+':
		s = s[1:]

	s = s.lstrip('0')
	if not s:
		return 0

	result = 0
	INT_MAX = 2 ** 31 - 1
	INT_MIN = -2 ** 31

	for char in s:
		if not char.isdigit():
			break
		result = result * 10 + int(char)

	result *= sign

	if result > INT_MAX:
		return INT_MAX
	if result < INT_MIN:
		return INT_MIN

	return result

if __name__ == '__main__':
	s1 = '42'          # 42
	s2 = '-042'        # -42
	s3 = '1337c0d3'    # 1337
	s4 = '0-1'         # 0
	s5 = 'слова и 987' # 0
	for s in [s1, s2, s3, s4, s5]:
		print(myAtoi(s))