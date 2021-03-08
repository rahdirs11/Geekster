n = int(input())

numbers = []
temp = n
zeros = 0
while temp > 0:
	d = temp % 10
	if d:
		numbers.append(d)
	else:
		zeros += 1
	temp //= 10

# print(numbers)

largest = sorted(numbers, reverse=True)
largest.extend([0] * zeros)
smallest = sorted(numbers)

# print(numbers)

while zeros >= 1:
	if len(smallest) == 1:
		smallest.append(0)
	else:
		smallest.insert(1, 0)
	zeros -= 1


# print(smallest, largest)
# print(int(''.join(map(str, smallest))), int(''.join(map(str, largest))))
print(int(''.join(map(str, largest))) - int(''.join(map(str, smallest))))