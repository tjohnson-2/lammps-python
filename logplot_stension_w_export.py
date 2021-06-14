import sys
import matplotlib.pyplot as plt
import numpy
ypoints = numpy.empty(0)
fp=open(sys.argv[1])
output = open(sys.argv[2], 'w')
line=fp.readline()
#print(line)
while line:
	#print(line)
	line=fp.readline()
	words = line.split()
	if (words[0]=="Step"):
		break
while line:
	line=fp.readline()
	words=line.split()
	if(words[0]=="Loop"):
		break
	xx = float((words[11]))
	yy = float((words[12]))
	zz = float((words[13]))
	stepone = (xx + yy) / 2
	stension = stepone - zz
	print(words[0],stension)
	output.write(words[0] + ' ' + str(stension) + '\n')
	ypoints = numpy.append(ypoints,float(stension))
fp.close()
output.close()
print(ypoints)
plt.plot(ypoints)
plt.show()
#print(words)