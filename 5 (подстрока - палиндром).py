import time


def find_palindromic_substring_1(s):
	if s:
		palindromic_substring = ''
		for h in range(len(s)):
			string = ''
			for i in range(h, len(s)):
				string += s[i]
				if len(string) > len(palindromic_substring) and string == ''.join(reversed(string)):
					palindromic_substring = string

		return palindromic_substring

	else:
		return 0


def find_palindromic_substring_2(s):
	if s:
		if len(s) == 1:
			return s

		ps = s[0]
		for k in range(len(s)):
			for i in range(k + 1, len(s)):
				if s[k:i+1] == s[k:i+1][::-1]:
					if len(s[k:i+1]) > len(ps):
						ps = s[k:i+1]
		return(ps)
	else:
		return 0


def find_palindromic_substring_3(s):
	if not s:
		return 0

	start = 0
	end = 0

	for i in range(len(s)):
		len1 = expand_around_center(s, i, i)  # для нечётной длины
		len2 = expand_around_center(s, i, i + 1)  # для чётной длины
		max_len = max(len1, len2)
		if max_len > end - start:
			start = i - (max_len - 1) // 2
			end = i + max_len // 2

	return s[start:end + 1] if (end - start + 1) > 1 else s[0] if s else 0


def expand_around_center(s, left, right):
	while left >= 0 and right < len(s) and s[left] == s[right]:
		left -= 1
		right += 1
	return right - left - 1

s = "borcdubqiupahpwjizjjbkncelfazeqynfbrnzuvbhjnyvrlkdyfyjjxnprfocrmisugizsgvhszooktdwhehojbrdbtgkiwkhpfjfcstwcajiuediebdhukqnroxbgtvottummbypokdljjvnthcbesoyigscekrqswdpalnjnhcnqrarxuufzzmkwizptyvjhpfidgmskuaggtpxqisdlyloznkarxofzeeyvteynluofuhbllyiszszbwnsglqjkignusarxsjvctpgiwnhdufmfpanfwxjwlmhgllzsmdpncbwnsbdtsvrjybynifywkulqnzprcxockbhrhvnwxrkvwumyieazclcviumvormynbryaziijpdinwatwqppamfiqfiojgwkvfzyxadyfjrgmtttvlgkqghgbcfhkigfojjkhskzenlpasyozcsuccdxhulcubsgomvcrbqwakrraesfifecmoztayrdjicypakrrneulfbqqxtrdelggedvloebqaztmfyfkhuonrognejxpesmwgnmnnnamvkxqvzrgzdqtvuhccryeowywmbixktnkqnwzlzfvloyqcageugmjqihyjxhssmhkfzxpzxmgpjgsduogfolnkkqizitbvvgrkczmojxnabruwwzxxqcevdwvtiigwckpxnnxxxdhxpgomncttjutrsvyrqcfwxhexhaguddkiesmfrqfjfdaqbkeqinwicphktffuwcazlmerdhraufbpcznbuipmymipxbsdhuesmcwnkdvilqbnkaglloswcpqzdggnhjdkkumfuzihilrpcvemwllicoqiugobhrwdxtoefynqmccamhdtxujfudbglmiwqklriolqfkknbmindxtljulnxhipsieyohnczddabrxzjmompbtnnxvivmoyfzfrxlufowtqzojfclmatthjtbhotdoheusnpirwicbtyrcuojsdmfcx"
s1 = 'cbbd'
s2 = "ba"
s3 = 'babad'
s4 = 'a'
s5 = 'dd'
s6 = 'abcda'
start = time.time()
print(find_palindromic_substring_1(s))
end = time.time()
res1 = end - start
print(res1)

start = time.time()
print(find_palindromic_substring_2(s))
end = time.time()
res2 = end - start
print(res2)

start = time.time()
print(find_palindromic_substring_3(s))
end = time.time()
res3 = end - start
print(res3)

print(min(res1, res2, res3))