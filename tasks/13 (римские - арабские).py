def romanToInt(s):
	roman_to_val = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000
	}
	total = 0
	prev_val = 0

	for char in reversed(s):  # Идём справа налево
		curr_val = roman_to_val[char]
		if curr_val < prev_val:
			total -= curr_val  # Вычитаем (например, IV = 5 - 1)
		else:
			total += curr_val  # Складываем (VI = 5 + 1)
		prev_val = curr_val

	return total

print(romanToInt('MCMXCIV'))