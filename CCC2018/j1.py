d1 = input("")
d2 = input("")
d3 = input("")
d4 = input("")

telemarketerCount = 0

if (d1 == 8 or d1 == 9):
	telemarketerCount += 1

if (d4 == 8 or d4 == 9):
	telemarketerCount += 1

if (d2 == d3):
	telemarketerCount += 1

if (telemarketerCount == 3):
	print "ignore"
else:
	print "answer"