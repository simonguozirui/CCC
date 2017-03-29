file = open("DATA41.txt")
data = file.read().split("\n")
file.close()
#print data

# data = file.read().split("\n")
# file.close()
# import random
# num = len(data)/2

# for i in range(num):
# 	l = int(data[i*2+0])
# 	list_data = data[i*2+1].split()
# 	for item in list_data:
# 		list_data[list_data.index(item)] = int(item)

# 	#print list_data
# 	newlist = sorted(list_data)
# 	#print newlist
# 	#print list_data.index(newlist[2])



# add = 0
# vlist = []
# biggest = 0
# for i in range(l):
# 	for j in range(list_data.index(list_data[i]), l):
# 		if j < l - 2:
# 			n = list_data[j + 1]
# 			a = list_data[j + 2]
# 		if n < a and a > biggest:
# 			add += 1
# 			biggest = a
# 	vlist.append(add)

# list_data = list_data[::-1]

# blist = []
# for i in range(l):
# 	for j in range(list_data.index(list_data[i]), l):
# 		if j < l - 2:
# 			n = list_data[j + 1]
# 			a = list_data[j + 2]
# 		if n < a and a > biggest:
# 			add += 1
# 	blist.append(add)



# for element in vlist:
# 	if list_data[vlist.index(element)] == 0 or list_data[vlist.index(element)] == 1:
# 		vlist[vlist.index(element)] += 1
# 	else:
# 		vlist[vlist.index(element)] += 2


import random
put = []
for i in range(10 ):
	put.append(random.randint(1,1000))

for i in sorted(put):
	print i
