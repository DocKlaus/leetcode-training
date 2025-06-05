def maxArea(height):
    lenght_list = len(height)
    S = 0
    for l1 in range(0, lenght_list):
        for l2 in range(l1 + 1, lenght_list):
            height_loc = min(height[l2], height[l1])
            length_loc = l2 - l1
            s_loc = length_loc * height_loc
            S = s_loc if s_loc > S else S

    return S


def maxArea_DeepSeek(height):
    left = 0
    right = len(height) - 1
    S = 0

    while left < right:
        height_loc = min(height[left], height[right])
        length_loc = right - left
        s_loc = length_loc * height_loc
        S = max(S, s_loc)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return S


list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(list))
print(maxArea_DeepSeek(list))
