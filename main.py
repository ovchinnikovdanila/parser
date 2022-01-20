import re
import csv
import os

def reader(filename):

	with open(filename) as f:

		inData = f.read()

		massWithoutSort = inData.split("@")

	return massWithoutSort

def razd(massWithoutSort):

	n = len(massWithoutSort)

	massA = [[] * 2] * n
	i = 0

	for item in massWithoutSort:
		massA[i] = item.split(",",1)
		if massA[i][0] == "3" or massA[i][0] == "100" or massA[i][0] == "140"	:
			i+=1


	k = 0
	n2 = 0
	for item in massA:
		if massA[n2]:
			n2+=1
	
	massB = [[] * 2] * n2

	for item in massA:
		if massA[k]:
			massB[k] = massA[k][1].split("=",1)
			massB[k][1] = re.sub("[^0-9]","",massB[k][1])
			k+=1

	nC = int(n2 / 3)
	massC = [[] * 3] * nC

	j = 0
	ii = 0
	for item in massB:
		if j % 3 == 0:
			massC[ii] = ["","",""]
			massC[ii][0] = massB[j][1][0]+massB[j][1][1]+massB[j][1][2]+massB[j][1][3]+"-"+massB[j][1][4]+massB[j][1][5]+"-"+massB[j][1][6]+massB[j][1][7]+" "+massB[j][1][8]+massB[j][1][9]+":"+massB[j][1][10]+massB[j][1][11]+":"+massB[j][1][12]+massB[j][1][13]
			massC[ii][1] = massB[j+1][1]
			massC[ii][2] = massB[j+2][1]
			ii+=1
		j+=1
	return(massC)

def write_csv(massC):

	with open('output.csv', "w") as csvfile:
		writer = csv.writer(csvfile)
		header = ["Version=1.0", "Generator=RuslanDat2koc","GeneratorVersion=0.1"]
		writer.writerow(header)

		i = 0
		for item in massC:
			if massC:
				rowC = [massC[i][0], "issue", massC[i][1], massC[i][2]]
				writer.writerow(rowC)
			i+=1

	thisFile = "output.csv"
	base = os.path.splitext(thisFile)[0]
	os.rename(thisFile, base + ".koc")

	i = 0
	for item in massC:
			print(item)


write_csv(razd(reader('circ.dat')))
