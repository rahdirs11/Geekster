def mergedIntervals(intervals: list) -> list:
	idx, i = int(), 1
	intervals.sort(key=lambda x: x[0])
	while i < len(intervals):
		if intervals[idx][1] >= intervals[i][0]:
			intervals[idx][1] = max(intervals[idx][1], intervals[i][1])
			intervals[idx][0] = min(intervals[idx][0], intervals[i][0])
		else:
			idx += 1
			intervals[idx] = intervals[i]
		i += 1



	return intervals[: idx + 1]


for x, y in mergedIntervals([[1, 3], [4, 6], [5, 7], [6, 8]]):
	print(x, y)






