import time
from itertools import product

def letterCombinations(digits):
	if not digits:
		return []

	digit_lett = {
		'2': 'abc',
		'3': 'def',
		'4': 'ghi',
		'5': 'jkl',
		'6': 'mno',
		'7': 'pqrs',
		'8': 'tuv',
		'9': 'wxyz'
		}
	all_combo = [""]
	for digit in digits:
		new_combo = []
		for combo in all_combo:
			for char in digit_lett[digit]:
				new_combo.append(combo + char)
		all_combo = new_combo



	return all_combo


from itertools import product


def letterCombinations_Serj(digits):
	if not digits:
		return []

	digit_lett = {
		'2': 'abc', '3': 'def', '4': 'ghi',
		'5': 'jkl', '6': 'mno', '7': 'pqrs',
		'8': 'tuv', '9': 'wxyz'
	}

	# Собираем только нужные списки букв
	letters = [digit_lett[d] for d in digits if d in digit_lett]

	# Генерируем все комбинации через product
	return [''.join(combo) for combo in product(*letters)]


digits = "23484952222656"
s1 = time.time()
letterCombinations(digits)
e1 = time.time()
print(e1-s1)

s2 = time.time()
letterCombinations_Serj(digits)
e2 = time.time()
print(e2-s2)