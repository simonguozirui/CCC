file = open("Next in line.txt")
youngest_children =  int(file.readline())
middle_children =  int(file.readline())
file.close()

print 2*middle_children - youngest_children