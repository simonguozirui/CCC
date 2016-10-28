file = open("Rovarspraket.txt")
english=  file.readline()
file.close()

consonant = "bcdfghjklmnpqrstvwxyz"
closestVowel =  "aaeeeiiiiooooouuuuuuu"
Rovarspraket = ""

for i in range(len(english)):
    t = consonant.find (english[i])
    Rovarspraket = Rovarspraket+ english[i]  
    if t > -1:# when t is a consonant
    	if t == 20: #when t is z
    		Rovarspraket = Rovarspraket + closestVowel [t] + "z"
        else: #when t is not z
        	Rovarspraket = Rovarspraket + closestVowel [t] + consonant[t+1]

print Rovarspraket