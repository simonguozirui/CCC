file = open("DATA21.txt")
num = int(file.readline())
data_input = file.read().split("\n\r")
file.close()

def judge(data):
	case_sum = 0
	name = []
	all_sum = []
	for i in range(len(data)):
		if len(data[i]) > 1:
			if str(data[i])[0] + str(data[i])[1] != "J ":
				name.append(str(data[i]))
				all_sum.append(case_sum)
				case_sum = 0
			else:
				case = data[i].split(" ")
				case.pop(0)
				current_sum = int(case[0]) + int(case[1]) + int(case[2])
				case_sum = case_sum + current_sum 

		elif data[i] == "*\r":
			all_sum.append(case_sum)

	all_sum.pop(0)
	current_max = 0
	max_index = 0
	for i in range(len(name)):
		if all_sum[i] > current_max:
			current_max = all_sum[i]
			max_index = i
	print name[max_index]
print data_input
judge(data_input)


