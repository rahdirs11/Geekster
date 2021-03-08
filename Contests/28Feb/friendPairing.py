def friendPairing(group, newGroup, dp={}):
	if [group, newGroup] in dp.keys():
		return dp[group, newGroup]

	if not group:
		if newGroup:
			return 1
		else:
			return 0

	dp[[group, newGroup]] = friendPairing(group - 1, newGroup + 1, dp) + friendPairing(group - 1, newGroup, dp)
	return dp[[group, newGroup]]


print(friendPairing(int(input()), 0)  +1)