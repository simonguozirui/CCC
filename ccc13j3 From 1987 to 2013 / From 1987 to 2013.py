#i have some logical error

file = open(" From 1987 to 2013.txt")
start_year =  int(file.readline()) + 1 
file.close()

distinct_year_found = False

while distinct_year_found == False:
	distinct_year_value = 0
	start_year_digit = str(start_year)
	for i in range(len(start_year_digit)-1):
		if start_year_digit[i] !=  start_year_digit[i+1]:
			distinct_year_value += 1
		else:
			distinct_year_value == False
	if distinct_year_value == len(start_year_digit)-1:
		print start_year
		distinct_year_found = True
	
	start_year += 1

