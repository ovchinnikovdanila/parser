import re
import csv
import os

def reader(filename):

	with open(filename, encoding="utf-8") as f:

		inData = f.read()

		massWithoutSort = inData.split("@")

	return massWithoutSort

def razd(massWithoutSort):

	n = 0
	for item in massWithoutSort:
		if item:
			n+=1

	massA = [[] * 2] * n
	
	i = 0
	for item in massWithoutSort:
		massA[i] = item.split(",",1)
		if massA[i][0] == "3" or massA[i][0] == "100" or massA[i][0] == "140"	:
			i+=1

	n = 0
	for item in massA:
		if item:
			n+=1

	
	massB = [[] * 2] * n

	i = 0
	for item in massA:
		if massA[i] and (massA[i][0] == "3" or massA[i][0] == "100" or massA[i][0] == "140") :
			massB[i] = massA[i][1].split("=",1)
			massB[i][1] = re.sub("[^0-9]","",massB[i][1])
			i+=1

	n = int(n / 3)
	massC = [[] * 3] * n

	j = 0
	i = 0
	for item in massB:
		if item:	
			if j % 3 == 0:
				massC[i] = ["","",""]
				massC[i][0] = massB[j][1][0]+massB[j][1][1]+massB[j][1][2]+massB[j][1][3]+"-"+massB[j][1][4]+massB[j][1][5]+"-"+massB[j][1][6]+massB[j][1][7]+" "+massB[j][1][8]+massB[j][1][9]+":"+massB[j][1][10]+massB[j][1][11]+":"+massB[j][1][12]+massB[j][1][13]
				massC[i][1] = massB[j+1][1]
				massC[i][2] = massB[j+2][1]
				i+=1
			j+=1	
	
	return(massC)

def issue_csv(massC):

	with open('issue.csv', "w") as csvfile:
		writer = csv.writer(csvfile, delimiter='\t')
		header = ["Version=1.0","Generator=RuslanDat2koc","GeneratorVersion=0.1"]
		writer.writerow(header)

		i = 0
		for item in massC:
			if massC:
				rowC = [massC[i][0],"issue",massC[i][1],massC[i][2]]
				writer.writerow(rowC)
			i+=1

	thisFile = "issue.csv"
	base = os.path.splitext(thisFile)[0]
	os.rename(thisFile, base + ".koc")

	massC.clear()

def return_csv(massC):


	thisFile = "return" + indexFile + ".csv"
	with open(thisFile, "w") as csvfile:
		writer = csv.writer(csvfile, delimiter='\t')
		header = ["Version=1.0","Generator=RuslanDat2koc","GeneratorVersion=0.1"]
		writer.writerow(header)

		i = 0
		for item in massC:
			if massC:
				rowC = [massC[i][0],"return",massC[i][2]]
				writer.writerow(rowC)
			i+=1

	base = os.path.splitext(thisFile)[0]
	os.rename(thisFile, base + ".koc")

	massC.clear()


# return_csv(razd(reader('acirc.dat')))
# issue_csv(razd(reader('circ.dat')))

dirname = './'
files = os.listdir(dirname)

for item in files:
	base = item.split(".",1)
	if base[1] == "dat":
		if base[0][0] == "a":
			if len(base[0]) != 5:
				indexFile = base[0].replace("acirc",'')
				return_csv(razd(reader(item)))
			if len(base[0])	== 5:
				indexFile = ""
				return_csv(razd(reader(item)))
		if base[0][0] == "c":
			indexFile = ""
			issue_csv(razd(reader(item)))
			print("issue " + item)


