def med1():
	merged = nums1 + nums2
	merged.sort()
	median_index = (len(merged) - 1) // 2
	if len(merged) % 2 == 0:
		median = (merged[median_index] + merged[median_index + 1]) / 2.0
	else:
		median = merged[median_index]

	return median


nums1 = [1,2]
nums2 = [3,4]
print(med1())