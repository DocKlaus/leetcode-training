def threeSumClosest(nums, target):
	sorted_nums = sorted(nums)
	length = len(nums)

	sum_default = sum(sorted_nums[:3])
	difference_default = abs(target - sum_default)
	closest_sum = sum_default

	for i_num1 in range(length - 2):

		i_num2 = i_num1 + 1
		i_num3 = length - 1

		while i_num2 < i_num3:
			sum_loc = sorted_nums[i_num1] + sorted_nums[i_num2] + sorted_nums[i_num3]
			difference = abs(target - sum_loc)
			if difference < difference_default:
				closest_sum = sum_loc
				difference_default = difference

			if sum_loc > target:
				i_num3 -= 1
			if sum_loc < target:
				i_num2 += 1
			if sum_loc == target:
				return sum_loc

	return closest_sum

nums = [1,3,4,7,8,9]
target = 15
print(threeSumClosest(nums, target))
# [[-1,-1,2],[-1,0,1]]