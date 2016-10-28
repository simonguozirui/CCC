#https://dmoj.ca/problem/ccc15j1
#February 18 is a special date for the CCC this year.
#Write a program that asks the user for a numerical month and numerical day of the month and then determines whether that date occurs before, after, or on February 18.
#If the date occurs before February 18, output the word Before.
#if the date occurs after February 18, output the word After.
#If the date is February 18, output the word Special.
file = open("Special Day.txt")
month =  int(file.readline())
day=  int(file.readline())
file.close()

if month <= 2 and day <18:
	print("Before")
elif month>=2 and day >18:
	print("After")
else:
	print("Special")