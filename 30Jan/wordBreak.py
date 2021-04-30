dictionary = {'i', 'like', 'sam', 'samsung', 'mobile', 'sung', 'ice', 'cream', 'and', 'icecream', 'man', 'go', 'mango'}


def wordBreak(string, result: str=""):
	if len(string) == 0:
		print(result)
		return

	for i in range(len(string) + 1):
		selected = string[: i]
		if selected in dictionary:
			remaining = string[i: ]
			wordBreak(remaining, result + " " + selected)


wordBreak('ilikeicecreamandmango')