file = open("DATA21.txt")
data_input = file.read()
file.close()
 
dataset = data_input.split("*")

for i in range(len(dataset)):
	dataset[i] = dataset[i].split("\r\n")

for i in range(len(dataset)):
	for j in range(len(dataset[i])-1):
		if dataset[i][j] == '':
			dataset[i].pop(j)
	dataset[i].pop(-1)

def judge_1(data):
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

		elif data[i] == "*∫":
			all_sum.append(case_sum)

	all_sum.pop(0)
	current_max = 0
	max_index = 0
	for i in range(len(name)):
		if all_sum[i] > current_max:
			current_max = all_sum[i]
			max_index = i
	print name[max_index]

def judge(data):
	case_sum = 0
	case_g =0
	case_f =0
	case_p =0
	name = []
	all_sum = []
	all_p = []
	all_f = []
	all_g = []
	for i in range(len(data)):
		if len(data[i]) > 1:
			if str(data[i])[0] + str(data[i])[1] != "J ":
				name.append(str(data[i]))
				all_sum.append(case_sum)
				all_p.append(case_p)
				all_f.append(case_f)
				all_g.append(case_g)
				case_sum = 0
				case_p = 0
				case_f = 0
				case_g = 0
			else:
				case = data[i].split(" ")
				case.pop(0)
				current_sum = int(case[0]) + int(case[1]) + int(case[2])
				current_g = int(case[2])
				current_f = int(case[1])
				current_p = int(case[0])
				case_sum = case_sum + current_sum 
				case_g = case_g + current_g
				case_f = case_f + current_f
				case_p = case_p + current_p

		elif data[i] == "*":
			all_sum.append(case_sum)
			all_p.append(case_p)
			all_f.append(case_f)
			all_g.append(case_g)

	#all_sum.pop(0)
	current_max = 0
	max_index = 0
	for i in range(len(name)):
		# if all_sum[i] > current_max:
		# 	current_max = all_sum[i]
		# 	max_index = i
		if all_sum[i] == current_max:
			if all_g[i] > all_g[max_index]:
				max_index = i

				if all_f[i] > all_f[max_index]:
					max_index = i
				else:
					if all_p[i] > all_p[max_index]:
						max_index = i
					else:
						print name[i] + ", "


	print name[max_index]

for x in range(len(dataset)):
	dataset[x].append("*")

for x in range(len(dataset)):
	if len(dataset[x])>0:
		judge_1(dataset[x])
