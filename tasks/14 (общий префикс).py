def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for str in strs[1:]:
        while str[: len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
