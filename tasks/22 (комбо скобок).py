def generateParenthesis(n: int) -> list[str]:
    result = []

    def recurs(current: str, open: int, close: int):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open < n:
            recurs(current + "(", open + 1, close)
        if close < open:
            recurs(current + ")", open, close + 1)

    recurs("", 0, 0)
    return result


print(generateParenthesis(3))
