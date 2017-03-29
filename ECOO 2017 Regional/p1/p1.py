file = open("DATA11.txt")
data = file.read().split("\n")
file.close()

y1c = 12
y2c = 10
y3c = 7
y4c = 5

num = len(data)/3

for i in range(num):
	cost = data[i*3+0]
	per = data[i*3+1].split()
	student = int(data[i*3+2])
	result = float(per[0])*student*y1c+float(per[1])*student*y2c+float(per[2])*student*y3c+float(per[3])*student*y4c
	result = result/2
	if int(result) < int(cost):
		print "YES"
	else:
		print "NO"
