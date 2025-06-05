class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s:
            res_substr = ""
            for h, head in enumerate(s):
                substr = head

                for i in range(h + 1, len(s)):
                    if s[i] in substr:
                        break
                    substr += s[i]

                if len(substr) > len(res_substr):
                    res_substr = substr

            return res_substr

        else:
            return 0


s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
