import time


def convert(s, numRows):
    rows = [[] for _ in range(numRows)]
    cur_row = 0
    flag_down = False

    for char in s:
        rows[cur_row].append(char)
        if cur_row == 0 or cur_row == numRows - 1:
            flag_down = not flag_down
        # if flag_down:
        # 	cur_row += 1
        # else:
        # 	cur_row -= 1
        cur_row += 1 if flag_down == True else -1

    result = []
    for row in rows:
        result.extend(row)

    return "".join(result)


def convert(s, numRows):
    rows = [[] for _ in range(numRows)]
    cur_row = 0
    flag_down = False

    for char in s:
        rows[cur_row].append(char)
        if cur_row == 0 or cur_row == numRows - 1:
            flag_down = not flag_down
        if flag_down:
            cur_row += 1
        else:
            cur_row -= 1
        # cur_row += 1 if flag_down == True else -1

    result = []
    for row in rows:
        result.extend(row)

    return "".join(result)


r1 = 0
r = 0

s = "PAYPALISHIRING"
numRows1 = 3
numRows2 = 4

for i in range(1000000):
    start1 = time.time()
    convert(s, numRows2)
    end1 = time.time()
    res1 = end1 - start1

    start = time.time()
    convert(s, numRows2)
    end = time.time()
    res = end - start

    if res > res1:
        r1 += 1
    else:
        r += 1

print(r1)
print(r)
