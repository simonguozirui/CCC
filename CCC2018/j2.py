n = input("")
yesterdayP = raw_input("")
todayP = raw_input("")

occupiedCount = 0

for i in range(n):
	if yesterdayP[i] == "C":
		if yesterdayP[i] == todayP[i]:
			occupiedCount += 1

print occupiedCount