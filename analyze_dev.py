#let's import some stuff
import argparse
import sys
import statistics
import matplotlib.pyplot as plt
import numpy

parser = argparse.ArgumentParser(description='Analysis Options')

#produce a log file from extracted data
parser.add_argument('-l',
	help='exports data from this script as a txt file',
	action='store_true',
	required=False)

args, unknown = parser.parse_known_args()

if(len(sys.argv) == 2):
	outfile = 'py_out.txt'
else:
	outfile = sys.argv[2]

fp=open(sys.argv[1])
if args.l:
	output = open(outfile, 'w')
line=fp.readline()
while line:
	line=fp.readline()
	words = line.split()
	if (words[0]=="Step"):
		break

numcol = len(words)
header = words

data = numpy.zeros((numcol,10000))
print(data.shape,data)

ln = 0

while line:
	line=fp.readline()
	words=line.split()
	if(words[0]=="Loop"):
		break

	print(words)
	for i in range(numcol):
		data[i][ln]=(float(words[i]))

	ln = ln +1

print("Number of lines of data:",ln)
print("# header average stdev")
for i in range(numcol):
	print(i,header[i],numpy.average(data[i,:ln]),numpy.std(data[i,:ln]))

exit()

#Mean output file writing
if args.ta and args.l:
	output.write('Temperature standard deviation of ' + sys.argv[1]  + ' is' + ' ' + str(mean))
if args.pa and args.l:
	output.write('Pressure standard deviation of ' + sys.argv[1]  + ' is' + ' ' + str(mean))
if args.va and args.l:
	output.write('Volume standard deviation of ' + sys.argv[1]  + ' is' + ' ' + str(mean))
if args.sa and args.l:
	output.write('Surface tension standard deviation of ' + sys.argv[1]  + ' is' + ' ' + str(mean))


#SD output file writing
if args.tdev and args.l:
	output.write('Temperature standard deviation of ' + sys.argv[1]  + ' is' + ' ' + str(deviation))
if args.pdev and args.l:
	output.write('Pressure standard deviation of ' + sys.argv[1]  + ' is' + ' ' + str(deviation))
if args.vdev and args.l:
	output.write('Volume standard deviation of ' + sys.argv[1]  + ' is' + ' ' + str(deviation))
if args.sdev and args.l:
	output.write('Surface tension standard deviation of ' + sys.argv[1]  + ' is' + ' ' + str(deviation))


fp.close()
if args.l:
	output.close()
if args.t or args.p or args.v or args.s:
	print(ypoints)
	plt.plot(ypoints)
	plt.show()
