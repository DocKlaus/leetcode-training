def fourSum(nums, target):
    nums.sort()
    length = len(nums)
    all_combo = []

    for i_num1 in range(length - 3):
        if i_num1 > 0 and nums[i_num1] == nums[i_num1 - 1]:
            continue

        for i_num2 in range(i_num1 + 1, length - 2):
            if i_num2 > i_num1 + 1 and nums[i_num2] == nums[i_num2 - 1]:
                continue

            i_num3 = i_num2 + 1
            i_num4 = length - 1

            while i_num3 < i_num4:
                sum_loc = nums[i_num1] + nums[i_num2] + nums[i_num3] + nums[i_num4]

                if sum_loc < target:
                    i_num3 += 1
                elif sum_loc > target:
                    i_num4 -= 1
                else:
                    combo = [nums[i_num1], nums[i_num2], nums[i_num3], nums[i_num4]]
                    if combo not in all_combo:
                        all_combo.append(combo)
                    while i_num3 < i_num4 and nums[i_num3] == nums[i_num3 + 1]:
                        i_num3 += 1
                    while i_num3 < i_num4 and nums[i_num4] == nums[i_num3 - 1]:
                        i_num4 -= 1

                    i_num3 += 1
                    i_num4 -= 1

    return all_combo


nums = [4, -3, -5, 4, 4, -1, 1, -4]
target = 4
print(fourSum(nums, target))
