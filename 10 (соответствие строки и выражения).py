def isMatch(s,p):
	m, n = len(s), len(p)
	dp = [[False] * (n + 1) for _ in range(m + 1)]
	print_dp(dp)
	dp[0][0] = True
	print_dp(dp)

	for j in range(1, n + 1):
		if p[j - 1] == '*':
			dp[0][j] = dp[0][j - 2]
			print_dp(dp)

	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
				dp[i][j] = dp[i - 1][j - 1]
				print_dp(dp)
			elif p[j - 1] == '*':
				dp[i][j] = dp[i][j - 2]
				print_dp(dp)
				if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
					dp[i][j] |= dp[i - 1][j]
					print_dp(dp)
	return dp[m][n]

def print_dp(dp):
	for el1 in dp:
		print(el1)
	print()

print(isMatch('aa', 'a*'))