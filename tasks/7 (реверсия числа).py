def reversed(x):
	sign = -1 if x < 0 else 1
	abs_x = abs(x)
	reversed_str = str(abs_x)[::-1]
	reversed_num = int(reversed_str) * sign

	if reversed_num < -2 ** 31 or reversed_num > 2 ** 31 - 1:
		return 0

	return reversed_num



x = -123
print(reversed(x))