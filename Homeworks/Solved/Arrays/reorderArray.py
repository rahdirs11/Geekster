def reorder(array: list, indices: list):
	for i in range(len(array)):
		array[i], array[indices[i]] = array[indices[i]], array[i]
		temp = indices[i]
		indices[i] = indices[indices[i]]
		indices[temp] = temp
		# print(array, indices)

	return array

def reorder2(array: list, indices: list) -> list:
	for i in range(len(array)):
		while indices[i] != i:
			oldI, oldE = indices[indices[i]], array[indices[i]]

			arr[indices[i]] = arr[i]
			indices[indices[i]] = indices[i]

			indices[i], array[i] = oldI, oldE

if __name__ == '__main__':
	array = [int(x) for x in input().split()]
	indices = [int(i) for i in input().split()]

	# print(array)

	# print(end="\n\n")

	reorder(array, indices)
	print(array, indices, sep="\n")