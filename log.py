import matplotlib.pyplot as plt
import numpy
ypoints = numpy.empty(0)
fp=open("formamide2.log")
line=fp.readline()
#print(line)
while line:
	#print(line)
	line=fp.readline()
	#words=split(line)
	words = line.split()
	if (words[0]=="Step"):
		break
while line:
	line=fp.readline()
	words=line.split()
	if(words[0]=="Loop"):
		break
	print(words[0],words[4])
	ypoints = numpy.append(ypoints,float(words[4]))
fp.close()
print(ypoints)
plt.plot(ypoints)
plt.show()
#print(words)
#print("done")