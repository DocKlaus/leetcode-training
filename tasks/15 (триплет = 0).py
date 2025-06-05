def threeSum(nums):
    sorted_nums = sorted(nums)
    length = len(nums)
    result = []

    for i_num1 in range(length - 2):

        i_num2 = i_num1 + 1
        i_num3 = length - 1

        while i_num2 < i_num3:
            sum = sorted_nums[i_num1] + sorted_nums[i_num2] + sorted_nums[i_num3]
            if sum > 0:
                i_num3 -= 1
            elif sum < 0:
                i_num2 += 1
            else:
                tr = [sorted_nums[i_num1], sorted_nums[i_num2], sorted_nums[i_num3]]
                if tr not in result:
                    result.append(tr)

                    i_num2 += 1
                    i_num3 -= 1

    return result


nums = [-2, 0, 1, 1, 2]
print(threeSum(nums))
# [[-1,-1,2],[-1,0,1]]
