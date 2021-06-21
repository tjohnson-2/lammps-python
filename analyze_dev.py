import argparse
import sys
import statistics
import matplotlib.pyplot as plt
import numpy

parser = argparse.ArgumentParser(description='Analysis Options')

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

data = numpy.zeros((numcol,100000))

ln = 0

while line:
	line=fp.readline()
	words=line.split()
	if(words[0]=="Loop"):
		break

	for i in range(numcol):
		data[i][ln]=(float(words[i]))

	ln_original = ln
	ln = ln +1

print("\n")
print("Number of steps:",ln_original)
print(f"{'#' : <5} {'Header' : <6} {'Average' : ^24} {'StDev' : ^6}")
for i in range(numcol):
	print(f"{i : <5} {header[i] :<8} {(numpy.average(data[i,:ln])) :>15.5f} {(numpy.std(data[i,:ln])) :>15.5f}",)
print("\n")

exit()

fp.close()

if args.l:
	output.close()
