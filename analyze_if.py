#let's import some stuff
import argparse
import sys
import statistics
import matplotlib.pyplot as plt
import numpy

parser = argparse.ArgumentParser(description='Analysis Options')

#produce one data point for each step
parser.add_argument('-t',
	help='step-by-step temperature',
	action='store_true',
	required=False)
parser.add_argument('-p',
	help='step-by-step pressure',
	action='store_true',
	required=False)
parser.add_argument('-v',
	help='step-by-step volume',
	action='store_true',
	required=False)
parser.add_argument('-s',
	help='step-by-step surface tension',
	action='store_true',
	required=False)

#average for whole log file
parser.add_argument('-ta',
	help='average temperature',
	action='store_true',
	required=False)
parser.add_argument('-pa',
	help='average pressure',
	action='store_true',
	required=False)
parser.add_argument('-va',
	help='average volume',
	action='store_true',
	required=False)
parser.add_argument('-sa',
	help='average surface tension',
	action='store_true',
	required=False)

#SD for whole log file
parser.add_argument('-tdev',
	help='temperature standard deviation',
	action='store_true',
	required=False)
parser.add_argument('-pdev',
	help='pressure standard deviation',
	action='store_true',
	required=False)
parser.add_argument('-vdev',
	help='volume standard deviation',
	action='store_true',
	required=False)
parser.add_argument('-sdev',
	help='surface tension standard deviation',
	action='store_true',
	required=False)

#produce a log file from extracted data
parser.add_argument('-l',
	help='exports data from this script as a txt file',
	action='store_true',
	required=False)

args, unknown = parser.parse_known_args()

#words list
#1 elapsed
#2 temperature
#3 pressure
#4 volume
#5 total energy
#6 kinetic energy
#7 potential energy
#8 e_mol
#9 e_pair
#10 Pxx
#11 Pyy
#12 Pzz
#13 Pxz
#14 Pxy
#15 Pyz

if args.t or args.p or args.v or args.s:
	ypoints = numpy.empty(0)

if args.ta or args.pa or args.va or args.sa:
	mean_list = []

if args.tdev or args.pdev or args.vdev or args.sdev:
	dev_list = []

fp=open(sys.argv[1])
if args.l:
	output = open('py_out.txt', 'w')
line=fp.readline()
while line:
	line=fp.readline()
	words = line.split()
	if (words[0]=="Step"):
		break
while line:
	line=fp.readline()
	words=line.split()
	if(words[0]=="Loop"):
		break

	#full temperature
	if args.t:
		v = words[2]
		print(words[0],words[2])
		if args.t and args.l:
			output.write(words[0] + ' ' + str(v) + '\n')

	#full pressure
	if args.p:
		v = words[3]
		print(words[0],words[3])
		if args.p and args.l:
			output.write(words[0] + ' ' + str(v) + '\n')

	#full volume
	if args.v:
		v = words[4]
		print(words[0],words[4])
		if args.v and args.l:
			output.write(words[0] + ' ' + str(v) + '\n')

	#full surface tension
	if args.s:
		xx = float(words[10])
		yy = float(words[11])
		zz = float(words[12])
		stepone = (xx + yy) / 2
		stension = stepone - zz
		v = stension
		print(words[0],stension)
		if args.s and args.l:
			output.write(words[0] + ' ' + str(v) + '\n')


	#average temperature
	if args.ta:
		mean_list.append(float(words[2]))

	#average pressure
	if args.pa:
		mean_list.append(float(words[3]))

	#average volume
	if args.va:
		mean_list.append(float(words[4]))

	#average surface tension
	if args.sa:
		xx = float(words[11])
		yy = float(words[12])
		zz = float(words[13])
		stepone = (xx + yy) / 2
		stension = stepone - zz
		mean_list.append(float(stension))


	#temperature SD
	if args.tdev:
		dev_list.append(float(words[2]))

	#pressure SD
	if args.pdev:
		dev_list.append(float(words[3]))

	#volume SD
	if args.vdev:
		dev_list.append(float(words[4]))

	#surface tension SD
	if args.sdev:
		xx = float(words[10])
		yy = float(words[11])
		zz = float(words[12])
		stepone = (xx + yy) / 2
		stension = stepone - zz
		dev_list.append(float(stension))


	if args.t or args.p or args.v or args.s:
		ypoints = numpy.append(ypoints,float(v))

if args.ta or args.pa or args.va or args.sa:
	mean = statistics.mean(mean_list)
	print(mean)

if args.tdev or args.pdev or args.vdev or args.sdev:
	deviation = statistics.pstdev(dev_list)
	print(deviation)

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