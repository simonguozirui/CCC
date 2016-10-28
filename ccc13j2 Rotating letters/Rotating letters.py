file = open("Rotating letters.txt")
word =  file.readline()
file.close()
right_letter = ["I","O","S","H","Z","X","N"]
print word
could_be_used = 0
for i in range(len(word)):
	for j in range(len(right_letter)):
		if word[i] == right_letter[j]:
			could_be_used +=1
if could_be_used == len(word):
	print "YES"
else:
	print "NO"