n = int(input(""))
inputTable = []
for i in range(n):
	inputTable.append(map(int, raw_input("").split(" ")))

def wInc(inputTable):
	initialwList = inputTable[0]
	if (initialwList[0] <= initialwList[1]):
		return True
	else:
		return False

def hInc(inputTable):
	initialhList = []
	for row in inputTable:
		initialhList.append(row[0])
	if (initialhList[0] <= initialhList[1]):
		return True
	else:
		return False


def tablePrint(printTable):
	if printTable != None:
		for row in printTable:
			printString = ""
			for element in row:
				printString += str(element)
				printString += " "
			printString = printString[:-1]
			print printString


if (wInc(inputTable) and hInc(inputTable)):
	#print "360"
	tablePrint(inputTable)
elif (wInc(inputTable) and not hInc(inputTable)):
	resultTable = []
	#print "270"
	#print len(inputTable[0])
	for i in range(len(inputTable[0])):
		resultTable.append([])
		for row in inputTable:
			resultTable[i].append(row[i])
	for result in resultTable:
		result.reverse()
	tablePrint(resultTable)
elif (not wInc(inputTable) and hInc(inputTable)):
	#print "90"
	resultTable = []
	#print len(inputTable[0])
	for i in range(len(inputTable[0])):
		resultTable.append([])
		for row in inputTable:
			resultTable[i].append(row[i])
	resultTable.reverse()
	tablePrint(resultTable)

elif (not wInc(inputTable) and not hInc(inputTable)):
	#print "180"
	inputTable.reverse()
	for row in inputTable:
		row.reverse()
	tablePrint(inputTable)
