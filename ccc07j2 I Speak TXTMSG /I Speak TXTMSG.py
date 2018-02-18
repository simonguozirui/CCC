file = open("I Speak TXTMSG.txt")
TXTMSG =  file.readlines()
file.close()

TXTMSG = map(lambda s: s.strip(), TXTMSG)

for i in range(len(TXTMSG)):
	if TXTMSG[i] == "CU":
		print ("see you")
	elif TXTMSG[i] == ":-)":
		print ("I'm happy")
	elif TXTMSG[i] == ":-(":
		print ("I'm unhappy")
	elif TXTMSG[i] == ";-)":
		print ("wink")
	elif TXTMSG[i] == ":-P":
		print ("stick out my tongue")
	elif TXTMSG[i] == "(~.~)":
		print ("sleepy")
	elif TXTMSG[i] == "TA":
		print ("totally awesome")
	elif TXTMSG[i] == "CCC":
		print ("Canadian Computing Competition")
	elif TXTMSG[i] == "CUZ":
		print ("because")
	elif TXTMSG[i] == "TY":
		print ("thank-you")
	elif TXTMSG[i] == "YW":
		print ("you're welcome")
	elif TXTMSG[i] == "TTYL":
		print ("talk to you later")
	else:
		print TXTMSG[i]
