def partition(array: list, k: int, idx: int=0, answer: list=[]):
	if idx == len(array):
		if len(answer) == k:
			for ans in answer:
				print(ans, end=' ')
			print()
		return

	if len(answer) == 0:
		answer.append([array[idx]])
		partition(array, k, idx + 1, answer)
		answer.pop(0)
	else:
		# print(len(answer), answer)
		for i in range(len(answer)):
			# print(answer[i], i)
			answer[i].append(array[idx])
			partition(array, k, idx + 1, answer)
			answer[i].pop(len(answer[i]) - 1)
		answer.append([array[idx]])
		partition(array, k, idx + 1, answer)
		answer.pop(len(answer) - 1)


partition([1, 2, 3, 4], 2)



