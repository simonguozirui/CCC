dbetweenCities = raw_input("").split(" ") 
cityLocationList = []

for i in range(len(dbetweenCities)+1):
	cityLocation = 0
	for j in range(i):
		cityLocation += int(dbetweenCities[j]) 
	cityLocationList.append(cityLocation)
dtoOtherCities = []

for baseCity in cityLocationList:
	dCurrentToOtherCities = []
	for i in range(len(cityLocationList)):
		dCurrentToOtherCities.append(abs(int(baseCity)-cityLocationList[i]))
		dCurrentToOtherCities.append(" ")
	dCurrentToOtherCities.pop(-1)
	printString = ""
	for element in dCurrentToOtherCities:
		printString += str(element)
	print printString
